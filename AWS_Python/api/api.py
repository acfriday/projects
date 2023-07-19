import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

teams = [
    {
        'id': 0,
        'name': 'Lakers',
        'championships': '17'},
    {   
        'id': 1,
        'name': 'Celtics',
        'championships': '17'},
    {   
        'id': 2,
        'name': 'Bulls',
        'championships': '6'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Test API</h1><p>This site is a prototype API for learning Flask and Python.</p>"


@app.route('/api/v1/resources/teams/all', methods=['GET'])
def api_all():
    return jsonify(teams)


app.run()