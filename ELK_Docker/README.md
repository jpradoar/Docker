# Docker ELK stack

### Logs
Apache2:8080 ---> logs ---> Logstash:5000

<hr>

### Ports
* 8080: Apache2
* 5000: Logstash.
* 9200: Elasticsearch
* 9300: Elasticsearch TCP transport
* 5601: Kibana

<hr>

### Run docker compose
<pre>
docker-compose up -d
</pre>

<hr>

### Kibana running
<p align="center">
  <img src="img01.png"/><br>
</p>

<hr>

### Python script (generate http request)
<p align="center">
  <img src="img2.png"/><br>
</p>
