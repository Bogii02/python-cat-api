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





if __name__ == '__main__':
    app.run(debug=True)
