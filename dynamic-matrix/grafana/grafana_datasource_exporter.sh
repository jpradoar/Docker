#!/bin/bash
mkdir -p data_sources && curl -s "http://localhost:3000/api/datasources"  -u admin:admin|jq -c -M '.[]'|split -l 1 - data_sources/

for i in data_sources/*; do \
    curl -X "POST" "http://localhost:3000/api/datasources" \
    -H "Content-Type: application/json" \
     --user admin:admin \
     --data-binary @$i
done

# Source
# https://rmoff.net/2017/08/08/simple-export-import-of-data-sources-in-grafana/
