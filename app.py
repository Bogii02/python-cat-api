import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import NotFound

CREATE_CATS_TABLE = (
    "CREATE TABLE IF NOT EXISTS cats (id SERIAL PRIMARY KEY, name VARCHAR(50), age INTEGER, color VARCHAR(50));"
)

INSERT_CAT = (
    "INSERT INTO cats (name, age, color) VALUES (%s, %s, %s) RETURNING id;"
)

GET_ALL_CATS = (
    "SELECT * FROM cats;"
)

SELECT_CAT_BY_ID = (
    "SELECT * FROM cats WHERE id = %s;"
)

DELETE_CAT_BY_ID = (
    "DELETE FROM cats WHERE id = %s;"
)

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.route('/')
def hello():
    return 'Welcome here!'


# should I make it into 1 function with an elif?
@app.route('/api/cats', methods=['POST'])
def create_cat():
    fields = ('name', 'age', 'color')

    data = request.json

    for key in fields:
        if key not in data:
            abort(400, f'Missing required field: {key}')

    for key in data.keys():
        if key not in fields:
            abort(400, f'Unexpected field: {key}')

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_CATS_TABLE)
                cursor.execute(INSERT_CAT, (data['name'], data['age'], data['color']))
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

        return jsonify(cats_data), 200

    except Exception as e:
        abort(500, f'Error adding cat: {str(e)}')


# should I send back 204?
@app.route('/api/cats/<int:id>', methods=['DELETE'])
def delete_one_cat_by_id(id):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_CAT_BY_ID, (id,))
                cat = cursor.fetchone()

                if cat:
                    cursor.execute(DELETE_CAT_BY_ID, (id,))
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


if __name__ == '__main__':
    app.run(debug=True)
