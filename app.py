from flask import flask
from flask import request
#from flask import jsonify
#from pymongo import MongoClient

app = Flask(__name__)

#client = MongoClient('mongodb://admin:root@ds125618.mlab.com:25618/mydatabase')
#db=client.mydatabase;

@app.route('/')
def homepage():
    return "MILKYWAY"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)