from flask import Flask
from hotpepper.request import request_hotpepper

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    data = request_hotpepper()
    return str(data)
