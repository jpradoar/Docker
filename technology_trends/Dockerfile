FROM ubuntu:16.04
MAINTAINER "Jonathan Prado <jpradoar @ gmail dot com>"

ADD tendencias.sh /
RUN apt-get update && apt-get install curl wget apache2 -y && chmod +x /tendencias.sh && /bin/bash /tendencias.sh 

EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
