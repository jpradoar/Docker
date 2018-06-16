FROM ubuntu:16.04

RUN apt-get update; apt-get install wget tar python -y && wget https://github.com/prometheus/prometheus/releases/download/v2.3.0/prometheus-2.3.0.linux-amd64.tar.gz && tar -xzvf prometheus-2.3.0.linux-amd64.tar.gz 

COPY ./prometheus.yml /prometheus-2.3.0.linux-amd64/prometheus.yml
RUN rm -rf prometheus-2.3.0.linux-amd64.tar; apt-get autoclean; apt-get clean all; apt-get autoremove; rm -rf /var/lib/apt/lists/*

EXPOSE 9090

CMD ["./prometheus-2.3.0.linux-amd64/prometheus", "--config.file=/prometheus-2.3.0.linux-amd64/prometheus.yml"]