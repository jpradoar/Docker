# Docker ELK stack

### Logs
Apache2:8080 ---> logs ---> Logstash:5000 <---> Kibana
apache2:8080 ---> logs ---> Elasticsearch <---> Grafana
All-containers <---> weave
<hr>

### Ports
* 8080: Apache2
* 8081: phpmyadmin
* 5000: Logstash
* 9200: Elasticsearch
* 9300: Elasticsearch TCP transport
* 5601: Kibana
* 3000: Grafana
* 4040: Weave

<hr>

### Run docker compose
<pre>
docker-compose up -d
</pre>

<hr>

### Apache webserver
<p align="center">
  <img src="img000.png"/><br>
</p>

<hr>

### Phpmyadmin with data
<p align="center">
  <img src="mysql.png"/><br>
</p>

### Kibana running
<p align="center">
  <img src="img01.png"/><br>
</p>

<hr>

### Grafana running
<p align="center">
  <img src="grafana.png"/><br>
</p>

<hr>

### Weave running
<p align="center">
  <img src="weave.png"/><br>
</p>

<hr>


### Python script (generate http request)
<p align="center">
  <img src="img2.png"/><br>
</p>


