import os
from flask import Flask
from flask import request
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
#import datetime
app = Flask(__name__)
CORS(app)
#test

#print(air_date)
client = MongoClient('mongodb://admin:root@ds125618.mlab.com:25618/mydatabase')
db=client.get_database('mydatabase')
@app.route('/')
def hello_world():
    return 'Hello World'


    
   
#@app.route('/val/<co>/<dust>',methods = ['GET'])
#def val(co=None,dust=None):
   
    #time_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')  + datetime.timedelta(hours=6)
    #print(time_date+" "+co+" "+dust)	
    #db.air_datas.insert_one({'time_date':time_date,'co': co,'dust':dust})
  
    #return time_date+" "+co+" "+dust
@app.route('/value',methods = ['GET','POST'])
def value():

    result=db.gasReadings.insert_one(content)
    return result;

if __name__ == '__main__':
    app.run(debug=True)
