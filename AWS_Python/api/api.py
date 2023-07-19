import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test API</h1><p>This site is a prototype API for learning Flask and Python.</p>"

app.run()