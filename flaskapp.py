import main
from flask import Flask, jsonify

app = Flask(__name__)

from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/spam/<string:email>')
def hello(email):
    result = main.spam_service(email)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
