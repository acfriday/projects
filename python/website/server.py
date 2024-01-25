from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html',first_name="Charlie")

@app.route('/Category_I_Languages')
def Category_I_Languages():
    return render_template('.html')

@app.route('/Category_II_Languages')
def Category_II_Languages():
    return render_template('.html')

@app.route('/Category_III_Languages')
def Category_III_Languages():
    return render_template('.html')

@app.route('/Category_IV_Languages')
def Category_IV_Languages():
    return render_template('.html')

if __name__ == '__main__':
    app.run(debug=True)