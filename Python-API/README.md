# Looking Glass API


### Build Dockerfile
	docker build --no-cache -t lgapi .

### Run api
	docker run -it -p 8088:8088 lgapi


### how to use and test
	curl -u admin:admin -H 'Content-Type: application/json' -X POST -d '{"data": "8.8.4.4" }'  127.0.0.1:8088/ping
<pre>
PING 8.8.4.4 (8.8.4.4): 56 data bytes
64 bytes from 8.8.4.4: seq=0 ttl=51 time=18.501 ms
64 bytes from 8.8.4.4: seq=1 ttl=51 time=18.065 ms
64 bytes from 8.8.4.4: seq=2 ttl=51 time=22.788 ms

--- 8.8.4.4 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 18.065/19.784/22.788 ms
</pre>

	curl -u admin:admin -H 'Content-Type: application/json' -X POST -d '{"data": "www.google.com" }'  127.0.0.1:8088/ping
<pre>
PING www.google.com (172.217.172.68): 56 data bytes
64 bytes from 172.217.172.68: seq=0 ttl=51 time=19.088 ms
64 bytes from 172.217.172.68: seq=1 ttl=51 time=32.200 ms
64 bytes from 172.217.172.68: seq=2 ttl=51 time=19.153 ms

--- www.google.com ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 19.088/23.480/32.200 ms
</pre>

	curl -u admin:admin -H 'Content-Type: application/json' -X POST -d '{"data": "www.google.com/rm\ -rf\ *" }'  127.0.0.1:8088/ping
<pre>
Bad Request
Failed to decode JSON object: Invalid \escape: line 1 column 28 (char 27)
</pre>




### Ref
- https://docs.python.org/3/library/http.client.html
- https://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
- https://stackoverflow.com/questions/28769023/get-output-of-system-ping-without-printing-to-the-console
- https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
- https://stackoverflow.com/questions/24708139/python-validate-a-url-as-having-a-domain-name-or-ip-address