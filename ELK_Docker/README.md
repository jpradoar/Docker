# Docker ELK stack

### Logs
Apache2:8080 ---> logs ---> Logstash:5000

### Ports
* 8080: Apache2
* 5000: Logstash.
* 9200: Elasticsearch
* 9300: Elasticsearch TCP transport
* 5601: Kibana

### Run docker compose
  $ docker-compose up -d


### Kibana running
<p align="center">
  <img src="img01.png"/><br>
</p>


### Python script (generate http request)
<p align="center">
  <img src="img2.png"/><br>
</p>
