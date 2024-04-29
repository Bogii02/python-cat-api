import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import NotFound



GET_ALL_CATS = (
    "SELECT * FROM cats;"
)

SELECT_CAT_BY_ID = (
    "SELECT * FROM cats WHERE id = %s;"
)


load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

FIELDS = ('name', 'age', 'color')


@app.route('/')
def hello():
    return 'Welcome here!'


# should I make it into 1 function with an elif?
@app.route('/api/cats', methods=['POST'])
def create_cat():
    create_cats_table = (
        "CREATE TABLE IF NOT EXISTS cats (id SERIAL PRIMARY KEY, name VARCHAR(50), age INTEGER, color VARCHAR(50));"
    )

    insert_cat = (
        "INSERT INTO cats (name, age, color) VALUES (%s, %s, %s) RETURNING id;"
    )

    data = request.json

    for key in FIELDS:
        if key not in data:
            abort(400, f'Missing required field: {key}')

    for key in data.keys():
        if key not in FIELDS:
            abort(400, f'Unexpected field: {key}')

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(create_cats_table)
                cursor.execute(insert_cat, (data['name'], data['age'], data['color']))
                cat_id = cursor.fetchone()[0]

        if cat_id:
            cat_dict = {
                "id": cat_id,
                "name": data['name'],
                "age": data['age'],
                "color": data['color']
            }
            return jsonify(cat_dict), 201

    except Exception as e:
        abort(500, f'Error getting cats: {str(e)}')


@app.route('/api/cats')
def get_all_cats():
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(GET_ALL_CATS)
                cats = cursor.fetchall()

        cats_data = []

        for cat in cats:
            cat_dict = {
                "id": cat[0],
                "name": cat[1],
                "age": cat[2],
                "color": cat[3]
            }
            cats_data.append(cat_dict)

        return jsonify({"cats": cats_data}), 200

    except Exception as e:
        abort(500, f'Error adding cat: {str(e)}')


# should I send back 204?
@app.route('/api/cats/<int:id>', methods=['DELETE'])
def delete_one_cat_by_id(id):
    delete_cat_by_id = (
        "DELETE FROM cats WHERE id = %s;"
    )

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_CAT_BY_ID, (id,))
                cat = cursor.fetchone()

                if cat:
                    cursor.execute(delete_cat_by_id, (id,))
                    return '', 204
                else:
                    raise NotFound()

    except NotFound as e:
        abort(404, f'There is no cat with id: {id}.\n {str(e)}')

    except Exception as e:
        abort(500, f'Error deleting cat: {str(e)}')


@app.route('/api/cats/<int:id>', methods=['GET'])
def get_one_cat_by_id(id):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_CAT_BY_ID, (id,))
                cat = cursor.fetchone()

            if cat:
                cat_dict = {
                    "id": cat[0],
                    "name": cat[1],
                    "age": cat[2],
                    "color": cat[3]
                }
                return jsonify(cat_dict), 200
            else:
                raise NotFound()

    except NotFound as e:
        abort(404, f'There is no cat with id: {id}.\n {str(e)}')

    except Exception as e:
        abort(500, f'Error getting cat: {str(e)}')


@app.route('/api/cats/<int:id>', methods=['PATCH'])
def update_cat(id):
    update_cat_query = (
        "UPDATE cats SET name=%s, age=%s, color=%s WHERE id=%s;"
    )

    data = request.json

    for key in data.keys():
        if key == 'id':
            abort(403, f'You do not have access to modify field: {key}.')
        if key not in FIELDS:
            abort(400, f'Unexpected field: {key}.')

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(update_cat_query, (data['name'], data['age'], data['color'], id))
                cursor.execute(SELECT_CAT_BY_ID, (id,))
                cat = cursor.fetchone()

                if cat:
                    cat_dict = {
                        "id": cat[0],
                        "name": cat[1],
                        "age": cat[2],
                        "color": cat[3]
                    }
                    return jsonify(cat_dict), 200
                else:
                    raise NotFound()

    except NotFound as e:
        abort(404, f'There is no cat with id: {id}.\n {str(e)}')

    except Exception as e:
        abort(500, f'Error getting cat: {str(e)}')


if __name__ == '__main__':
    app.run()
