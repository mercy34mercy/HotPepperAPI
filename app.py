from crypt import methods
from databasefiles.alltime import alltime
from flask import Flask
from flask import request
from databasefiles.inserttime import insertime
from hotpepper.request import request_hotpepper

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    data = request_hotpepper()
    return data

@app.route('/time',methods=['POST'])
def time():
    json_data = request.json
    response = insertime(json_data["resid"],json_data["time"])
    return response

@app.route('/admin',methods=['GET'])
def admin():
    response = alltime()
    return str(response)

