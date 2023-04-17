from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3000},
    {"id":2, "name":"Americano", "price":4000},
    {"id":3, "name":"CafeLatte", "price":5000}
]

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id" : 4,
        "name" : request_data["name"],
        "price" : request_data["price"]
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/')
def hello_flask():
    return "Hello World!"

if __name__ == '__main__':
    app.run()