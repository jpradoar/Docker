# NGINX proxy

### Build image
docker build -t proxy . 

### Run example
<pre>
docker run -itd --name server1 -p 1111:80 nginx
docker run -itd --name server2 -p 2222:80 nginx
docker run -itd --name proxy -p 80:80 -p 8081:8081 -p 8082:8082 proxy
# -p :80:80 is not necessary, only to show nginx index
</pre>



