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
        url_index = ['index.php', 'about.html', 'services.html', 'products', 'product-details.html', 'blog-home.html', 'blog-single.html', 'contact.html', 'elements', 'nodata.html', ' ',]
        ref_index = ['blog.example.com/post/01/', 'news.supernews.com/index', 'curl.com', 'blasite.com/bla/index', 'cucubird.com/post/1']
        agent = ['Mozilla/5.0', 'Chrome/4.1', 'Opera', 'Safari/1.2', 'Android 6.0.1','Mobile; rv:61.0']
        command="curl -s --referer "+(random.choice(ref_index))+"  -A "+(random.choice(agent))+" http://"+RequestIP+"/"+(random.choice(url_index))+" >/dev/null"
        output="http://"+RequestIP+"/"+(random.choice(url_index))
        os.system(command)
        print output


for x in range(0, request_num):
        magic()
        tiempo()
