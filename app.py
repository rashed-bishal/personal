from flask import Flask
from flask import request
import pymongo

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)