# Simpe Python API


### Build Dockerfile
	docker build --no-cache -t pyapi .

### Run api
	docker run -it -p 8088:8088 pyapi


### Test ping IP without login
	curl -H 'Content-Type: application/json' -X GET  127.0.0.1:8088/?ping=8.8.4.4
		Login fail: User and/or Password are wrong.


### Test ping IP with login
	curl -u admin:admin -H 'Content-Type: application/json' -X GET  127.0.0.1:8088/?ping=8.8.4.4
		PING 8.8.4.4 (8.8.4.4) 56(84) bytes of data.
		64 bytes from 8.8.4.4: icmp_seq=1 ttl=51 time=20.8 ms
		64 bytes from 8.8.4.4: icmp_seq=2 ttl=51 time=21.2 ms
		64 bytes from 8.8.4.4: icmp_seq=3 ttl=51 time=16.1 ms
		--- 8.8.4.4 ping statistics ---
		3 packets transmitted, 3 received, 0% packet loss, time 2004ms
		rtt min/avg/max/mdev = 16.059/19.372/21.224/2.348 ms


### Test ping url
	curl -u admin:admin -H 'Content-Type: application/json' -X GET  127.0.0.1:8088/?ping=www.google.com
		PING 172.217.172.100 (172.217.172.100) 56(84) bytes of data.
		64 bytes from 172.217.172.100: icmp_seq=1 ttl=51 time=17.4 ms
		64 bytes from 172.217.172.100: icmp_seq=2 ttl=51 time=18.0 ms
		64 bytes from 172.217.172.100: icmp_seq=3 ttl=51 time=20.1 ms
		--- 172.217.172.100 ping statistics ---
		3 packets transmitted, 3 received, 0% packet loss, time 2002ms
		rtt min/avg/max/mdev = 17.367/18.498/20.080/1.152 ms


### Test ping url with command (rm -rf /)   ;)
	curl -u admin:admin -H 'Content-Type: application/json' -X GET  127.0.0.1:8088/?ping='www.google.com/\ rm \-rf \.'
		Error response
		Error code: 400
		Message: Bad request syntax ('GET /?ping=www.google.com/\\ pwd HTTP/1.1').
		Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.




### http logs
172.17.0.1 - - [14/Jan/2020 21:18:46] "GET /?ping=8.8.4.4 HTTP/1.1" 200 -
172.17.0.1 - - [14/Jan/2020 21:18:51] "GET /?nmap=8.8.4.4 HTTP/1.1" 200 -
172.17.0.1 - - [14/Jan/2020 21:19:01] "GET /?traceroute=8.8.4.4 HTTP/1.1" 200 -
172.17.0.1 - - [14/Jan/2020 21:19:11] "GET /?nslookup=8.8.4.4 HTTP/1.1" 200 -
172.17.0.1 - - [14/Jan/2020 21:19:20] "GET /?host=8.8.4.4 HTTP/1.1" 200 -
172.17.0.1 - - [14/Jan/2020 21:19:36] "GET /?dig=8.8.4.4 HTTP/1.1" 200 -
