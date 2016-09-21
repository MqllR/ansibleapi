# Ansible API

This project aimed to provide a simple API Rest to run Ansible playbooks and tasks. The project is fully dockerized with ansible's sources.

## Installation

  * With docker

Get image :
```
docker pull registry.gitlab.com/mqll/ansibleapi
```
And run it :
```
docker run -d -v pathtosshconf:/root/.ssh \
    -v pathtoplaybooks:/opt/playbooks \
    -v pathtoroles:/opt/roles \
    -e "PYTHONPATH=/opt/ansible/lib" \
    -p 80:8000 registry.gitlab.com/mqll/ansibleapi
```
Edit settings_local.py with your DB credentials and run:
```
docker exec -i CONTAINERID bash -c 'cd /opt/app && python manage.py migrate'
docker exec -it CONTAINERID bash -c 'cd /opt/app && python manage.py createsuperuser'
docker exec -i CONTAINERID bash -c 'cd /opt/app && python manage.py fillplaybook'
```

## How it works?

First, you need to fill the database with hosts and users via the admin URL http://myserver/admin/

Then, send request like below to play playbooks :
```
curl -H 'APIKEY: AECWD3T42GS435CA3R' -d '{ "playbook": "upgrade-package.yml", "hosts": ["108.121.120.64"]}' http://myserver/api/run/playbook/
```
or simple tasks :
```
curl -H 'APIKEY: AECWD3T42GS435CA3R' -d '{ "tasks": [{ "action": { "module": "setup", "args": {}}}], "hosts": ["108.121.120.64"]}' http://myserver/api/run/tasks/
