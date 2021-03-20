FROM alpine:latest
RUN apk update; apk add curl bash jq tzdata
ADD getversions.sh /
ENTRYPOINT ["/bin/bash", "/getversions.sh"]
