import werkzeug.exceptions
from flask import Flask, jsonify, request, abort

import data_manager
import utils

app = Flask(__name__)

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
    cat = data_manager.get_cat_by_id(id)
    data = request.json

    for key in data.keys():
        if key not in FIELDS:
            abort(400, f'Unexpected field: {key}')

    for key in FIELDS:
        if key not in data:
            abort(400, f'Missing required field: {key}')

    if cat is None:
        abort(404, f'Cat with id: {id} was not found')
    else:
        updated_cat = data_manager.update_cat_by_id(data, id)

    return updated_cat, 200


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
