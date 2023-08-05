import datetime

from flask import Flask, request, jsonify

app = Flask("HomeWork App")


@app.route('/', methods=['GET', 'POST'])
def greet():
    print(request)
    if request.method == 'GET':
        query = """
        <center><h1>Hello World!</h1></center>
        
        <center><h3>This is a test site!</h3></center>
        """
        return query
    else:
        return 'POST Hello World!'


@app.route('/api/names/<name>')
def names(name):
    print(request.args)
    return jsonify({name: len(name)})

@app.route('/api/dates/<date>')
def date_analsys(date: str):
    try:
        ts = datetime.datetime.strptime(date, '%d-%m-%Y')
        ret_val = {"date": ts}
        if 'season' in request.args and request.args['season'].lower() == 'true':
            season = 'winter'
            if ts.month in (3, 4, 5):
                season = 'spring'
            elif ts.month in (6, 7, 8):
                season = 'summer'
            elif ts.month in (9, 10, 11):
                season = 'autman'
            ret_val.update({'season': season})
        return ret_val

    except ValueError:
        return {'error': "bad date format"}, 400



@app.route('/api/users', methods=['POST'])
def create_user():
    print(request.form)
    print(request.data)
    print(request.json)
    return {}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
