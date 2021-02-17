#!/usr/bin/python3
from flask import Flask, jsonify, request, Response
from functools import wraps
import os
# import httplib # (for python2)
import http.client  # (for python3)
import logging
import socket
from subprocess import Popen, PIPE
import json
# for telnet support
import getpass
import telnetlib

app = Flask(__name__)

# FUNCTIONS ---------------------------------------------------------------------------------------------


def check_auth(username, password):
    # Check if username and password are admin:admin.
    # Here you can use a function to check this data on remote database
    return username == 'admin' and password == 'admin'

# Example:
# curl -u 'admin:admin' -H 'Content-Type: application/json' -X GET  x.x.x.x:8089/?ping=www.google.com
#


def not_authenticate():
    # If user or pass are wrong, send an error message
    return Response('Login fail: User and/or Password are wrong!\n', 401,  {'WWW-Authenticate': 'Basic realm="Login Required"'})


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

# -----------------------------------------------------------------------


@app.route('/help', methods=['GET'])
def get_help():
    return "Options:\n\n/ping,\n/nmap,\n/traceroute,\n/nslookup,\n/host,\n/dig\n,\n/dig\n"

# -----------------------------------------------------------------------


@app.route('/', methods=['GET'])
@requires_auth
def run_command():

    if 'ping' in request.args:
        p = Popen(['ping', '-c', '1', '-W', '1', '-w', '1', request.args['ping']],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, bufsize=-1, start_new_session=False, pass_fds=())
        output, err = p.communicate(
            b"input data that is passed to subprocess' stdin")

    if 'traceroute' in request.args:
        p = Popen(['traceroute', request.args['traceroute']],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(
            b"input data that is passed to subprocess' stdin")

    if 'nslookup' in request.args:
        p = Popen(['nslookup', request.args['nslookup']],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(
            b"input data that is passed to subprocess' stdin")

    if 'host' in request.args:
        p = Popen(['host', request.args['host']],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(
            b"input data that is passed to subprocess' stdin")

    if 'dig' in request.args:
        p = Popen(['dig', request.args['dig']],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(
            b"input data that is passed to subprocess' stdin")


    if 'nmap' in request.args:
        # Nmap tarda aproximadamente 1 minuto x request(FIXEAR)
        # print("entro.........")
        # p = Popen(['nmap', request.args['nmap']],
        #           stdin=PIPE, stdout=PIPE, stderr=PIPE)
        # output, err = p.communicate(
        #     b"input data that is passed to subprocess' stdin")
        return("Feature not supported yet, comming soon")

    if 'telnet' in request.args:
        return("Feature not supported yet, comming soon")



    print("ERROR CODE: ", p.returncode)
    print("OUTPUT: ", output)

    if(p.returncode == 2):
        return("ocurrió un error ejecutando el comando.")

    return output


# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=False)
