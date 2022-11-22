# npmGrafStats
NginxProxyManager Grafana Statistic.

This project analyzes the logs of the Nginx Proxy Manager and exports it to InfluxDB.
It saves following Data:
- source IP
- target IP in your home network set in NPM
- the targeted domain
- the Data of the source IP from GeoLite2-City.mmdb
  - Country
  - Coordinates
  - City

This project is a modified clone of  https://github.com/Festeazy/nginxproxymanagerGraf and independent of https://github.com/jc21/nginx-proxy-manager.

To the Original Project following changes were made:
- the new log format and only the proxy-host*-access.log from NPM are used
- Domains now allow a - in the domain
- no subdomains or subdomains up to 3 levels extra (sub.sub.sub.domain.tld)
- the targeted internal ip is loged

## required things for the installation

1) create influxdb nginxproxymanagergraf
2) Create username and password for nginxproxymanagergraf  
3) get your GeoLite2-City.mmdb google is your friend upload it somewhere where you'll find it
4) Start the docker container or docker compose with ajusted settings
5) Add data source into grafana
6) Import the dashboard file or download it with the ID:  and set the new data source (Nginx Proxy Manager.json)

## start docker on the same host where nginx proxy manger runs
- Set Directory to NPM logs and to the GeoLite2-City.mmdb
- Set Influx settings
- Set HOME_IPS to your External/Public IP
  - if multiple external IP Addresses separated them with \| 
```
docker run --name npmgraf -it -d
-v /home/docker/nginx-proxy-manager/data/logs:/logs \
-v /home/docker/nginx-proxy-manager/GeoLite2-City.mmdb:/GeoLite2-City.mmdb \
-e HOME_IPS=external IP \
-e INFLUX_USER=admin \
-e INFLUX_PW=password \
-e INFLUX_DB=nginxproxymanagergraf \
-e INFLUX_HOST=192.168.0.189 \
-e INFLUX_PORT=8086 \
smilebasti/npmgrafstats
```
### Docker Compose file
```
version: '3'
services:
  npmgraf:
    image: smilebasti/npmgrafstats
    environment:
      - HOME_IPS=extrenal IP 
      - INFLUX_USER=admin 
      - INFLUX_PW=password
      - INFLUX_DB=nginxproxymanagergraf
      - INFLUX_HOST=192.168.0.189
      - INFLUX_PORT=8086
    volumes:
      - /home/docker/nginx-proxy-manager/data/logs:/logs
      - /home/docker/nginx-proxy-manager/GeoLite2-City.mmdb:/GeoLite2-City.mmdb
```

## GeoLite2-City.mmdb Auto update
Use this Docker Compose file to automaticly update the GeoLite2-City.mmdb
Set your ID and Key!
```
Still coming
```

## Grafana world map
Import nginxproxymanager.json file to grafana or use the Grafana Dashboard-ID:


Obviously I'd appreciate help or any feedback :) 
Hope you enjoy

How it looks in the end:


## Dev info/changes made to original
- args parssed sendips.sh to Getipinfo.py: 1. Outside IP 2. Domain 3. length 4. Target IP
- These Domain only registered for me : .env.de, config.php.com(.de,.org)
- Add Domains to Dashboard
- Did NPM change the log format? -> to access.log
- exclude external Ip
- add apk grep for --line-buffered as not included in bash in busybox -> overflow -> process stopped

### Todo list
- use logtime and not hosttime to save the stats
- upgrade to influx 2 - see project evijana2/nginxproxmanagerGraf on github
