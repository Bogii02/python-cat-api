import os

import psycopg2
import werkzeug.exceptions
from dotenv import load_dotenv
from flask import Flask, jsonify, request, abort

import data_manager
import utils

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


@app.route('/api/cats', methods=['POST'])
def create_cat():
    data = request.json

    for key in FIELDS:
        if key not in data:
            abort(400, f'Missing required field: {key}')

    for key in data.keys():
        if key not in FIELDS:
            abort(400, f'Unexpected field: {key}')

    data_manager.create_db_table()

    cat = data_manager.create_cat(data)

    return jsonify(cat), 201


@app.route('/api/cats')
def get_all_cats():
    cats = data_manager.get_all_cats()
    return jsonify(cats), 200


@app.route('/api/cats/<int:id>', methods=['DELETE'])
def delete_one_cat_by_id(id):
    cat = data_manager.get_cat_by_id(id)

    if cat is None:
        abort(404, f'Cat with id: {id} was not found')
    else:
        data_manager.delete_cat_by_id(id)

    return '', 204


@app.route('/api/cats/<int:id>', methods=['GET'])
def get_one_cat_by_id(id):
    cat = data_manager.get_cat_by_id(id)

    if cat is None:
        abort(404, f'Cat with id: {id} was not found')

    return jsonify(cat), 200


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

    except Exception as e:
        abort(500, f'Error getting cat: {str(e)}')


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request_error(error):
    response_body = utils.create_error_message("invalid input", error)
    return response_body, 400


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found_error(error):
    response_body = utils.create_error_message("data could not be found", error)
    return response_body, 404


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_internal_server_error(error):
    response_body = utils.create_error_message("failed to establish a connection with the database", error)
    return response_body, 500


if __name__ == '__main__':
    app.run(debug=True)
