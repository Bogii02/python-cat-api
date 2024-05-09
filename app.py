from flask import Flask, jsonify, request, abort

import data_manager
import response_validation

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome here!'


@app.route('/api/cats', methods=['POST'])
def create_cat():
    data = request.json
    data_manager.create_db_table_if_not_exists()

    if not response_validation.check_field_is_in_response(data):
        abort(400, 'Missing required field')

    elif not response_validation.check_unexpected_field_not_in_response(data):
        abort(400, 'Unexpected field')
    else:
        cat = data_manager.create_cat(data)
        return jsonify(cat), 201


@app.route('/api/cats')
def get_all_cats():
    cats = data_manager.get_all_cats()
    return jsonify(cats), 200


@app.route('/api/cats/<int:id>', methods=['DELETE'])
def delete_one_cat_by_id(id):
    cat = data_manager.get_cat_by_id(id)

    if response_validation.check_cat_exists(cat):
        data_manager.delete_cat_by_id(id)
    else:
        abort(404, f'Cat with id: {id} was not found')

    return '', 204


@app.route('/api/cats/<int:id>', methods=['GET'])
def get_one_cat_by_id(id):
    cat = data_manager.get_cat_by_id(id)

    if response_validation.check_cat_exists(cat):
        return jsonify(cat), 200
    else:
        abort(404, f'Cat with id: {id} was not found')


@app.route('/api/cats/<int:id>', methods=['PATCH'])
def update_cat(id):
    cat = data_manager.get_cat_by_id(id)
    data = request.json

    if not response_validation.check_field_is_in_response(data):
        abort(400, 'Missing required field')

    elif not response_validation.check_unexpected_field_not_in_response(data):
        abort(400, f'Unexpected field')

    elif not response_validation.check_cat_exists(cat):
        abort(404, f'Cat with id: {id} was not found')

    updated_cat = data_manager.update_cat_by_id(data, id)

    return jsonify(updated_cat), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
