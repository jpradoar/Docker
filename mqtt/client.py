#!/usr/bin/python
import paho.mqtt.client as mqtt
import datetime 
import requests

broker_address = "127.0.0.1"
broker_portno = 1883
cli_id = "00001"
subscr = "test"
xtopic = "test"

def display_ip():
    # Function To Print GeoIP Latitude & Longitude
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' + my_ip + '.json')
    geo_data = geo_request.json()
    print ({'lat': geo_data['latitude'], 'lon': geo_data['longitude']})

def send_message():
    client = mqtt.Client()
    client.connect(broker_address, broker_portno)
    client.subscribe(subscr)
    client.publish(topic = xtopic, payload = "This is a test Message from "+ cli_id + ": " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    send_message()
#
