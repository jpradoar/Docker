FROM ubuntu:18.04

WORKDIR /root

COPY ./config/server/* /root/
COPY ./config/aws_credentials/* /root/.aws/

RUN apt-get update; apt-get install -y awscli \
&& apt-get autoclean \
&& apt-get autoremove --purge \
&& rm -rf /var/lib/apt/lists/* 

ENTRYPOINT [ "./prometheus" ]

