#!/bin/bash
>tendencias.txt
clear
date=$(date)
echo -e "================================= \n" $date "\n=================================\n " >> tendencias.txt

#lista_tecnologias=("Linux" "Docker" "Kubernetes" )
lista_tecnologias=("Linux" "Docker" "Kubernetes" "AWS" "Ansible" "Terraform" "Bash" "Python" "nosql" "Redis" "RabbitMQ" "Elasticsearch" "Prometheus" "Grafana" "Kibana" "InfluxDB" "GitLab" "GitHub" "Jenkins")


for i in "${lista_tecnologias[@]}"
do
	sitios=(
	"http://www.universobit.com.ar/empleos-busqueda-$i.html"
	"https://www.computrabajo.com.ar/ofertas-de-trabajo/?q=$i"
        "http://www.bumeran.com.ar/buenos-aires/empleos-busqueda-$i.html"
        "https://www.zonajobs.com.ar/ofertas-de-trabajo-$i.html"
        "http://ar.jobomas.com/Trabajo-de-$i"
        "https://ar.indeed.com/Empleos-de-"$i"-en-Provincia-de-Buenos-Aires"
	)
	for x in "${sitios[@]}"
	do
		numero=$(curl -s -R $x | grep -i $i | wc -l )
		resultado="$x  =======> $numero"
		echo $resultado; echo $resultado >> tendencias.txt
	done
done


echo -e "\n================================= \n" ESTADISTICAS "\n=================================\n " >> tendencias.txt

echo "<!DOCTYPE html><html><body><br><div align='center'><h1>Technologies popularity</h1><pre>" >index.html
for z in "${lista_tecnologias[@]}"
do
        cat tendencias.txt | sort -n | grep $z | cut -d'>' -f2 | awk '{sum += $1}END{print sum}' | sed 's/$/ '$z' /g' |tee -a tendencias.txt index.html
#	cat tendencias.txt | sort -n | grep $z | cut -d'>' -f2 | awk '{sum += $1}END{print sum}' | sed 's/$/ '$z' /g' >> index.html 
done
echo "</pre><br><h1>Show in Google Trends</h1>" >> index.html

for t in "${lista_tecnologias[@]}"
do
        echo '<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/1644_RC01/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"'$t'","geo":"","time":"today 5-y"}],"category":0,"property":""}, {"exploreQuery":"date=today%205-y&q=Linux","guestPath":"https://trends.google.com:443/trends/embed/"}); </script> '>> index.html
done
echo "</div></body></html>" >> index.html

#cat tendencias.txt
cp -rp index.html /var/www/html/index.html
