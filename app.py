import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://admin:root@ds125618.mlab.com:25618/mydatabase')
db=client.get_database('mydatabase')

@app.route('/')
def homepage():
    return "BANGLADESH"

@app.route('/value',methods = ['GET','POST'])
def value():
    content = request.json
    result=db.gasReadings.insert_one(content)
    return result;

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)