from flask import Flask, jsonify, request
import datetime

app = Flask("example_app")


@app.route('/', methods=['GET', 'POST'])
def greet():
    print(request)
    if request.method == 'GET':
        return 'GET Hello World!'
    else:
        return 'POST Hello World!'

@app.route('/api/new_users')
def greet_name_query():
    print(request.args)
    return jsonify({"Your name": request.args['name'],
                    "Your Address": request.args['address']})

@app.route('/api/users/<string:name>/addresses/<int:address_id>')
def greet_name(name, address_id):
    return jsonify({"Your name": name,
                    "Your Address": address_id})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)


