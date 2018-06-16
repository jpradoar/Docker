FROM ubuntu:16.04
# Based on https://github.com/att-comdev/prometheus-openstack-exporter

RUN apt-get update; apt-get install -y python-dateutil python-requests python-simplejson python-yaml python-prometheus-client; apt-get clean; apt-get autoclean; apt-get clean all; apt-get autoremove; rm -rf /var/lib/apt/lists/*
RUN mkdir -p /srv
COPY ./exporter/ /srv/exporter
EXPOSE 9103 
CMD ["python","/srv/exporter/main.py"]

