#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import User, Host

from extras.ansibleplay import AnsiblePlaybook
from extras.ansibletasks import AnsibleTasks
from extras.ansibleauth import AnsibleAuth
from extras.utils import *

from pprint import pprint
import json

@csrf_exempt
def run_playbook(request):
    """
    Method to run playbook
    POST content need to have this syntax:

    { 
        "playbook": "/home/mql/dev/ansible/playbooks/upgrade.yml",
        "hosts": ["mql__mql-ovh-mail1"]
    }
    """

    # check method, header...
    validate_request(request)

    # Get a json object
    data = json_data(request)

    # Build the struct
    struct = {
        'playbook': 	unicode,
        'hosts':        list,
    }

    # TODO IMPLEMENT OPTS for ID, IP...
    if 'opts' in data:
        struct['opts'] = dict

    # Check the validity of content
    validate_data(data, struct)

    # Check for authorization
    auth = AnsibleAuth(request.META['HTTP_APIKEY'])

    for host in data['hosts']:
        if not auth.isauthorized(host):
            raise AnsibleException('Not authorized', error=401)

    anspb = AnsiblePlaybook(hosts=data['hosts'], playbook=data['playbook'])
    anspb.run()

    return JsonResponse(
                anspb.getResult()
           )

@csrf_exempt
def run_tasks(request):
    """
    Method to run tasks
    POST content need to have this syntax: 
    { 
        "tasks": [{ "action": { "module": "setup", "args": {}}}],
        "hosts": ["mql__mql-ovh-mail1"]
    }
    """

    # check method, header...
    validate_request(request)

    # Get a json object
    data = json_data(request)
    pprint(data)

    # Build the struct
    struct = {
        'tasks': 	list,     # [{ 'action': { 'module': 'command', 'args': { 'cmd': 'ip a' } } }]
        'hosts':        list,
    }

    # TODO IMPLEMENT OPTS for ID, IP...
    if 'opts' in data:
        struct['opts'] = dict

    # Check the validity of content
    validate_data(data, struct)

    # Check for authorization 
    auth = AnsibleAuth(request.META['HTTP_APIKEY'])

    for host in data['hosts']:
        if not auth.isauthorized(host):
            raise AnsibleException('Not authorized', error=401)

    anspb = AnsibleTasks(hosts=data['hosts'], tasks=data['tasks'])
    anspb.run()

    return JsonResponse(
            anspb.getResult()
           )
