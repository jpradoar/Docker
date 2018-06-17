FROM alpine:3.7

RUN apk update; apk add wget tar python -y && wget https://github.com/prometheus/prometheus/releases/download/v2.3.0/prometheus-2.3.0.linux-amd64.tar.gz && tar -xzvf prometheus-2.3.0.linux-amd64.tar.gz 

COPY ./prometheus.yml /prometheus-2.3.0.linux-amd64/prometheus.yml
RUN rm -rf prometheus-2.3.0.linux-amd64.tar

EXPOSE 9090

CMD ["./prometheus-2.3.0.linux-amd64/prometheus", "--config.file=/prometheus-2.3.0.linux-amd64/prometheus.yml"]
