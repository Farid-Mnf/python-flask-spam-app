import main
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/spam/<string:email>')
def hello(email):
    result = main.spam_service(email)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
