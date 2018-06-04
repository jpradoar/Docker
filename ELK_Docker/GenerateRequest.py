#!/usr/bin/python
import os
import random
import time

RequestIP="localhost:8080"
request_num=random.randint(50,350)

def tiempo():
        for i in xrange(10000):
                n = random.random()
                print "Miliseconds: " + str(n) + "\n"
                time.sleep(n)
                return

def magic():
        url_index = ['index.html', 'about.html', 'services.html', 'products.html', 'product-details.html', 'blog-home.html', 'blog-single.html', 'contact.html', 'elements.html', 'nodata.html', ' ',]
        agent = ['Mozilla/5.0', 'Chrome/4.1', 'Opera', 'Safari/1.2']
        command="curl -s -A "+(random.choice(agent))+" http://"+RequestIP+"/"+(random.choice(url_index))+" >/dev/null"
        output="http://"+RequestIP+"/"+(random.choice(url_index))
        os.system(command)
        print output


for x in range(0, request_num):
        magic()
        tiempo()
