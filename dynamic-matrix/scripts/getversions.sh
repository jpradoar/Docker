#!/bin/bash
while true; do
	sleep 15
	#data=$(curl -sH "PRIVATE-TOKEN: asd123" $giturl |jq -r '.' )
	data=$(curl -s https://raw.githubusercontent.com/jpradoar/Docker/master/dynamic-matrix/versions.json |jq -r '.' )
	#--------------------------------------------------
	# PENDIENTE DE MEJORAR ESTA COSA TAN FEA !!!
	#-------------------------------------------------
	datenow=$(date --utc +%FT%T)
	environment=$(echo $data|jq -r .versions.environment)
	component01=$(echo $data|jq -r .versions.app.component01)
	component02=$(echo $data|jq -r .versions.app.component02)
	component03=$(echo $data|jq -r .versions.app.component03)
	component04=$(echo $data|jq -r .versions.app.component04)
	k8s=$(echo $data|jq -r .versions.aws.kubernetes)
	rds=$(echo $data|jq -r .versions.aws.rds)

	curl -XPOST -sH 'Content-Type: application/json' http://elasticsearch:9200/versions/status/?pretty=true \
	-d '{ "environment": "'$environment'", "component01": "'$component01'", "component02": "'$component02'", "component03": "'$component03'", "component04": "'$component04'", "Kubernetes": "'$k8s'", "Rds": "'$rds'", "@timestamp" : "'$datenow'" }' |jq -r .

done




