import os
from flask import Flask
from flask import request
#from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
#CORS(app)

@app.route('/')
def homepage():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)