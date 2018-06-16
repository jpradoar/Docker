# Openstack Prometheus monitor

### Logic
<pre>
.
├── data
├── docker-compose.yml
├── exporter
│   ├── Dockerfile
│   └── exporter
│       ├── base.py
│       ├── check_os_api.py
│       ├── cinder_services.py
│       ├── hypervisor_stats.py
│       ├── main.py
│       ├── neutron_agents.py
│       ├── nova_services.py
│       ├── oscache.py
│       └── osclient.py
├── grafana
│   ├── grafana_datasource_exporter.sh
│   └── provisioning
│       ├── dashboards
│       │   ├── dashboard.yml
│       │   └── openstack.json
│       └── datasources
│           └── datasource.yml
├── prometheus
│   ├── Dockerfile
│   └── prometheus.yml
│
└── README.md
</pre>

<hr>

### Docker compose
<pre>
Docker Images: 	Ubuntu 16.04 (Oficial)
prometheus: 	Prometheus v2.3 (Oficial release)
exporter: 	Some python scripts (based on: rakeshpatnaik/prometheus-openstack-exporter)
grafana: 	Grafana latest (docker grafana/grafana)
</pre>

</hr>

### Infra
<pre>
Openstack: [Server]
Exporter: [container] Use openstack api to get data and publish on port 9103
Prometheus: [container] Get data from exporter container and publish on port 9090
Grafana: [container] Get data from datasource prometheus and generate dashboars

 -------------             -----------------      -------------------      ----------------
 | Openstack | <-- API --> | Exporter:9103 | ---> | Prometheus:9090 | ---> | Grafana:3000 | 
 -------------             -----------------      -------------------      ----------------

</pre>

<hr>

### Resources (avg normal use)
<pre>
Grafana:
	memory: 30Mb
	CPU: 0.7%

</pre>
