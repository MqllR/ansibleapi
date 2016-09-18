#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse

from api.extras.exceptions import AnsibleException
from api.models import Log

import json
import time

def validate_request(request):
    """
    Get an HttpRequest object and check for global structure.
    Raise an exception if not satistfay
    """
    
    if not request.method == 'POST':
        raise AnsibleException('Bad method')

    # Is empty?
    if request.META['CONTENT_LENGTH'] == '':
        raise AnsibleException('Empty request')

    # API KEY
    if not 'HTTP_APIKEY' in request.META:
        raise AnsibleException('Error: HTTP_APIKEY is missing')


def validate_data(json_data, struct):
    """
    Get a json object and a dict and compare each other.
    Raise an exception if not satistfay
    """

    if len(json_data) != len(struct):
        raise AnsibleException('unexpected number of params')

    for k, v in struct.items():
        
        if not k in json_data:
            raise AnsibleException('%s is missing' % k)

        if type(json_data[k]) is not v:
            raise AnsibleException('%s is not %s' % (k, v))

def json_data(request):
    """
    Get an HttpRequest object and return a json object
    Raise an exception if not satistfay
    """

    try:
        json_data = json.loads(request.body)

    except Exception as e:
        raise AnsibleException(str(e))

    return json_data

def log(user, host, action):
    """
    Log actions
    """

    mytime = time.strftime('%Y/%m/%d %H:%M:%S')
    Log(time=mytime, action=action, user=user, host=host).save()
