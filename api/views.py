#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import User, Host

from extras.ansibleplay import AnsiblePlaybook
from extras.utils import *

import json

@csrf_exempt
def run(request):
    """
    Method to run playbook
    """

    resp = validate_request(request)
    if resp:
        return resp 

    data = json_data(request)
    if type(data) is JsonResponse:
        return data


    # Build the struct
    struct = {
	    'playbook': 	unicode,
		'hosts': 		list,
    }

    # TODO IMPLEMENT OPTS for ID, IP...
    if 'opts' in data:
        struct['opts'] = dict

    resp = validate_data(data, struct)
    if resp:
        return resp 

    anspb = AnsiblePlaybook(hosts=data['hosts'], playbook=data['playbook'])
    # TODO CATCH OUTPUT IN AnsiblePlaybook TO BUILD HttpJsonResponse
    anspb.run()

    return JsonResponse({'Check': 'OK'})
    

@csrf_exempt
def test(request):
    print(request.META)
    return JsonResponse({'coucou': 'hello'})
