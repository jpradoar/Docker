FROM ubuntu:16.04
RUN apt-get update && apt-get install curl bash util-linux -y
ADD getdolar.sh /
ENTRYPOINT ["/bin/bash", "/getdolar.sh"]
