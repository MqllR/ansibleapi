#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import User, Host

from extras.ansibleplay import AnsiblePlaybook
from extras.utils import *

import json

@csrf_exempt
def run_playbook(request):
    """
    Method to run playbook
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

    anspb = AnsiblePlaybook(hosts=data['hosts'], playbook=data['playbook'])
    # TODO CATCH OUTPUT IN AnsiblePlaybook TO BUILD HttpJsonResponse
    anspb.run()

    return JsonResponse({'Check': 'OK'})

# DEBUG
@csrf_exempt
def test(request):
    print(request.META)
    return JsonResponse({'coucou': 'hello'})
