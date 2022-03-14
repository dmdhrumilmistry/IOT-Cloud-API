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
    
        #  Format : 
        # { 
        #   KEY : 
        #       { 
        #           NODE : 
        #                   { 
        #                       SENSOR : [(data, time, date)]
        #                   }
        #       }
        # }
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
    response = make_response("<h1>IOT Cloud API</h1>")
    return response, 200


@app.route(f'/{config.AUTH_KEY}/push_data', methods=['POST'])
def push_data():
    if request.method == "POST":
        try:
            data = request.json
            return jsonify({"push_status":__save_pushed_data(data)}), 200

        except Exception as e:
            print(e)
            return jsonify({'Error':'Invalid Data'}), 400

    return jsonify({'Error':'Invalid Request'}), 400
