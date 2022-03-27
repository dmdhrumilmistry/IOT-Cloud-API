'''
module: app
description:
-------------------------
 API for IOT cloud
-------------------------
Accepts data from the node in form of json data and stores it in local icdb file

Stored Data Format in icdb file:
{ 
  KEY : 
      { 
          NODE : 
                  { 
                      SENSOR : [(data, time, date)]
                  }
      }
}
'''

from flask import Flask, jsonify, make_response, request
from database import DB

import config
import datetime
import os


app = Flask(__name__)
app.config['ENV'] = 'development'
db_path = os.path.join(os.getcwd(), 'pushed_data')
db = DB(db_path)


def __save_pushed_data(data:dict) -> bool:
    '''
    description:
        Saves pushed data from client to database

    params:
        data (dict) : data in form of dictionary

    returns:
        bool
    '''
    status = True
    try:
        dbdata = db.read_data()
        node = data.get("node", "Err")
        sensor = data.get("sensor", "Err")
        sensor_data = data.get("sen_data", "Err")

        if config.AUTH_KEY not in dbdata.keys():
            dbdata[config.AUTH_KEY] = dict()
        if node not in dbdata[config.AUTH_KEY].keys():
            dbdata[config.AUTH_KEY][node] = dict()
        if sensor not in dbdata[config.AUTH_KEY][node].keys():
            dbdata[config.AUTH_KEY][node][sensor] = list()
    
      
        time = datetime.datetime.now()
        data_tuple = (str(time.strftime("%m %d %Y")), str(time.strftime("%H:%M:%S")), sensor_data)
        dbdata[config.AUTH_KEY][node][sensor].append(data_tuple)

        db.data = dbdata
        db.write_data()

    except Exception as e:
        status = False
    return status


@app.route('/', methods=['POST', 'GET'])
def home():
    '''
    description:
        return Home page html code and status code

    params: 
        None
    
    returns:
        Response, int
    '''
    response = make_response("<h1>IOT Cloud API</h1>")
    return response, 200


@app.route(f'/{config.AUTH_KEY}/push_data', methods=['POST'])
def push_data():
    '''
    description:
        handles client pushed json data from the node, 
        saves in the database, and returns status back
        to the user in json format along with status code.

    params:
        None
    
    returns:
        Response, int
    '''
    if request.method == "POST":
        try:
            data = request.json
            print(data)
            return jsonify({"push_status":__save_pushed_data(data)}), 200

        except Exception as e:
            print(e)
            return jsonify({'Error':'Invalid Data'}), 400

    return jsonify({'Error':'Invalid Request'}), 400


@app.route(f'/{config.AUTH_KEY}/get_data/', methods=['POST', 'GET'])
def get_data():
    '''
    description:
        handles client request to retrieve data from 
        the database, returns data in json format along
        with status code.

    params:
        None

    returns:

    '''
    return jsonify(db.data)