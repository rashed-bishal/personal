import os
from flask import Flask
from flask import request
from flask import jsonify
#from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
#CORS(app)

client = MongoClient('mongodb://admin:root@ds125618.mlab.com:25618/mydatabase')
db=client.get_database('mydatabase')

@app.route('/')
def homepage():
    return "Hello"


@app.route('/value',methods=['GET','POST'])
def value():
    content = request.json
    result=db.gasReadings.insert_one(content)
    return content

if __name__ == '__main__':
    app.run(debug=True)