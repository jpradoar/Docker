#!/usr/bin/python3
from flask import Flask, jsonify, request, Response
from functools import wraps
import os
# import httplib # (for python2)
import http.client # (for python3)
import logging
import socket
import subprocess

app = Flask(__name__)

def check_auth(username, password):
    # Check if username and password are admin:admin. 
    # Here you can use a function to check this data on remote database
    return username == 'admin' and password == 'admin'

def not_authenticate():
    # If user or pass are wrong, send an error message
    return Response('Login fail: User and/or Password are wrong.  Chupala gato!\n', 401,  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return not_authenticate()
        return f(*args, **kwargs)
    return decorated
#----------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET'])
def hello():
    return "Hi, Im a LookinGlass API \n"

#---------------------------------------------------------------------------------------------------------
@app.route('/ping', methods=['POST']) # POST to http://apiserver/ping
@requires_auth # This call auth function
def ping():
    if not request.json or not 'data' in request.json: # If request is not a json, the request is dropped
        return "Invalid key, the key needs to be a json o need to be 'data' \n" # And return an error message
    else:
        data = request.json['data'] # Capture value of json in "data" 
        try: 
            socket.gethostbyname(data) # Check if value is an IP or URL 
            response = subprocess.check_output(['ping', '-c', '3', data],stderr=subprocess.STDOUT, universal_newlines=True) # Hago un ping al destino
            return response
            print(data)
        except:
            return "Resource invalid '" + data + "' is not valid \n"  # Print an error
#-----------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=False) # Open a webserver on port 8088






