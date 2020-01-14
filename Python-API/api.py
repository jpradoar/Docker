#!/usr/bin/python3
from flask import Flask, jsonify, request, Response
from functools import wraps
import os
# import httplib # (for python2)
import http.client # (for python3)
import logging
import socket
import subprocess
import json

app = Flask(__name__)

# FUNCTIONS ---------------------------------------------------------------------------------------------

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


# ROUTES-----------------------------------------------------------------------------------------------------
@app.route('/info', methods=['GET'])
def hello():
    return "- Host performs DNS lookups, converting domain names to IP addresses and vice versa. \n- Ping is usually used as a simple way to verify that a computer can communicate over the network with another computer or network device.\n- Traceroute is a command which can show you the path a packet of information takes from your computer to one you specify. It will list all the routers it passes through until it reaches its destination, or fails to and is discarded.\n- Nmap is used for exploring networks, perform security scans, network audit and finding open ports on remote machine.\n- Dig is a too used for querying Domain Name System (DNS) name servers. It is useful for verifying and troubleshooting DNS problems and also to perform DNS lookups and displays the answers that are returned from the name server that were queried.\n\nWhen you have selected the type of query and node, and filled the additional parameter field, press Run."

#-----------------------------------------------------------------------
@app.route('/help', methods=['GET'])
def get_help():
    return "Options:\n\n/ping,\n/nmap,\n/traceroute,\n/nslookup,\n/host,\n/dig\n"

#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
@requires_auth
def run_command():
    if 'ping' in request.args:
        response = subprocess.check_output(['ping', '-c', '3', socket.gethostbyname(str(request.args['ping']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
    if 'nmap' in request.args:
        response = subprocess.check_output(['nmap', socket.gethostbyname(str(request.args['nmap']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
    if 'traceroute' in request.args:
        response = subprocess.check_output(['traceroute', socket.gethostbyname(str(request.args['traceroute']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
    if 'nslookup' in request.args:
        response = subprocess.check_output(['nslookup', socket.gethostbyname(str(request.args['nslookup']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
    if 'host' in request.args:
        response = subprocess.check_output(['host', socket.gethostbyname(str(request.args['host']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
    if 'dig' in request.args:
        response = subprocess.check_output(['dig', socket.gethostbyname(str(request.args['dig']) ) ],stderr=subprocess.STDOUT, universal_newlines=True)
    return response


#-----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=False) # Open a webserver on port 8088


