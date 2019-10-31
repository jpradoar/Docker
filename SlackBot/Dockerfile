FROM alpine:3.3
MAINTAINER "Jonathan Prado <jpradoar \ gmail dot com>"

ADD slackbot.py /
RUN apk update && apk add --update python python-dev py-pip && pip install --upgrade pip && pip install slackclient; export LC_ALL=C;

CMD [ "python", "./slackbot.py" ]
