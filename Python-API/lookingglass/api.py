#!/usr/bin/python3
from flask import Flask, jsonify, request, Response
from functools import wraps
import os
import http.client
import logging
import socket
import subprocess
import json
from logging.config import dictConfig

app = Flask(__name__)


# FUNCTIONS ---------------------------------------------------------------------------------------------

def check_auth(username, password):
    # Check if username and password are admin:admin. 
    # Here you can use a function to check this data on remote database
    # PENDING: validate with mariadb
    return username == 'admin' and password == 'admin'

def not_authenticate():
    # If user or pass are wrong, send an error message
    return Response('Login fail: User and/or Password are wrong.\n', 401,  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return not_authenticate()
        return f(*args, **kwargs)
    return decorated


# This function will be used to write data on DB for statistics
def show_test():
        for a in request.args:
            test = a
        for key in request.args:
            destino = request.args.get(key)
        print(test+":"+destino)
        # Write data in MariaDB

# ROUTES-----------------------------------------------------------------------------------------------------
@app.route('/info', methods=['GET'])
def get_help():
    return "Simple API test.\n\nOptions:\n\n/ping,\n/nmap,\n/traceroute,\n/nslookup,\n/host,\n/dig\n\n curl url:8088/?ping=8.8.8.8\n curl url:8088/?ping=www.google.com"

#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
@requires_auth
def run_command():
    if 'ping' in request.args:
        response = subprocess.check_output(['ping', '-c', '3', socket.gethostbyname(str(request.args['ping']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
        show_test()
    if 'nmap' in request.args:
        response = subprocess.check_output(['nmap', socket.gethostbyname(str(request.args['nmap']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
        show_test()
    if 'traceroute' in request.args:
        response = subprocess.check_output(['traceroute', socket.gethostbyname(str(request.args['traceroute']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
        show_test()
    if 'nslookup' in request.args:
        response = subprocess.check_output(['nslookup', socket.gethostbyname(str(request.args['nslookup']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
        show_test()
    if 'host' in request.args:
        response = subprocess.check_output(['host', socket.gethostbyname(str(request.args['host']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
        show_test()
    if 'dig' in request.args:
        response = subprocess.check_output(['dig', socket.gethostbyname(str(request.args['dig']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
        show_test()
    return response


#---LOGS --------------------------------------------------------------------------------------------------------
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# OPTIONAL LOG TO FILE
#logging.basicConfig(level=logging.INFO,
#                    format='%(asctime)s %(levelname)-8s %(message)s',
#                    datefmt='%a, %d %b %Y %H:%M:%S',
#                    filename='/tmp/datadogapi.log',
#                    filemode='w')

#-----------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=False) # Open a webserver on port 8088
    handler = logging.StreamHandler(sys.stdout)
    app.logger.addHandler(handler)


