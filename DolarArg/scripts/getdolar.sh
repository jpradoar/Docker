curl -H 'Content-Type: application/json' -XPUT http://elasticsearch:9200/dolar?pretty=true -d '{"settings" : {"index" : {"number_of_replicas" : 0 } }}'
while true; do
	preciodolar=$(curl -s 'https://www.preciodolar.com.ar/index.html' -H 'authority: www.preciodolar.com.ar' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'  |grep '<td class="Estilo4">'|cut -d">" -f2 |cut -d"<" -f1 |tail -1)
	curl -H 'Content-Type: application/json' -XPOST http://elasticsearch:9200/dolar/status/?pretty=true -d '{"source": "preciodolar.com.ar", "price" : '$preciodolar', "@timestamp" : "'$(date --utc +%FT%T.%3NZ)'"}'	
	sleep 5
	dolarhoy=$(curl -s http://www.dolarhoy.com/Usd |grep Venta |cut -d"$" -f2 |grep span |cut -d"<" -f1 |cut -d" " -f2|sed 's/,/./g')
	curl -H 'Content-Type: application/json' -XPOST http://elasticsearch:9200/dolar/status/?pretty=true -d '{"source": "dolarhoy.com", "price" : '$dolarhoy', "@timestamp" : "'$(date --utc +%FT%T.%3NZ)'"}'
	sleep 5
        bancogalicia=$(curl -s 'https://dolaraldia.com/bancosargentina/banco-galicia/' -H 'authority: dolaraldia.com' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' |grep CotizacionBanco |grep "Banco Galicia"|cut -d"/" -f4- |cut -d"<" -f1 |cut -d" " -f2-)   
        curl -H 'Content-Type: application/json' -XPOST http://elasticsearch:9200/dolar/status/?pretty=true -d '{"source": "BancoGalicia", "price" : '$bancogalicia', "@timestamp" : "'$(date --utc +%FT%T.%3NZ)'"}'
	echo "'{"source": "BancoGalicia", "price" : '$bancogalicia', "@timestamp" : "$(date --utc +%FT%T.%3NZ)"}'"
        sleep 5
done
