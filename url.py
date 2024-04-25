from flask import Flask, jsonify, request, abort

app = Flask(__name__)

id_counter = 3
cats = [
    {
        "id": 1,
        "name": "Edi",
        "age": 15,
        "color": "multicolored"
    },
    {
        "id": 2,
        "name": "Töki",
        "age": 6,
        "color": "black"
    }
]


@app.route('/')
def hello():
    return 'Welcome here!'


@app.route('/api/cats')
def get_cats():
    return cats


@app.route('/api/cats', methods=['POST'])
def create_cat():
    global id_counter
    fields = ('name', 'age', 'color')

    data = request.json

    for key in fields:
        if key not in data:
            return abort(400, f'Missing required field: {key}')

    for key in data.keys():
        if key not in fields:
            abort(400, f'Unexpected field: {key}')

    cat = {
        'id': id_counter,
        'name': data['name'],
        'age': data['age'],
        'color': data['color']
    }

    id_counter += 1

    cats.append(cat)

    return jsonify(cats), 201


if __name__ == '__main__':
    app.run(debug=True)
