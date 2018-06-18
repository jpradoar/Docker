FROM alpine:3.7
# Based on https://github.com/att-comdev/prometheus-openstack-exporter

RUN apk update; apk add py-dateutil py-requests py-simplejson py-yaml py-pip; pip install prometheus_client
RUN mkdir -p /srv
COPY ./exporter/ /srv/exporter
EXPOSE 9103 
CMD ["python","/srv/exporter/main.py"]

