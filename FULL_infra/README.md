# Docker devops stack

### Logs
* Apache2:8080 ---> logs ---> Logstash:5000 <---> Kibana
* apache2:8080 ---> logs ---> Elasticsearch <---> Grafana
* All-containers <---> weave
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
* 8888: Gitweb (git)
* 8088/443/50000: Jenkins
* 10022: Ansible (pendig) 
<hr>

### Run docker compose
<pre>
docker-compose up -d
</pre>

<hr>

### Apache webserver
<p align="center">
  <img src="images/img000.png"/><br>
</p>

<hr>

### Phpmyadmin with data
<p align="center">
  <img src=images/mariadb.png"/><br>
</p>

### Kibana running
<p align="center">
  <img src="images/img01.png"/><br>
</p>

<hr>

### Grafana running
<p align="center">
  <img src="images/grafana.png"/><br>
</p>

<hr>

### Weave running
<p align="center">
  <img src="images/weave.png"/><br>
</p>

<hr>

### Jenkins running
<p align="center">
  <img src="images/jenkins.png"/><br>
</p>

<hr>

### Gitserver running
<p align="center">
  <img src="images/gitweb.png"/><br>
</p>

<hr>


### Python script (generate http request)
<p align="center">
  <img src="images/img2.png"/><br>
</p>


