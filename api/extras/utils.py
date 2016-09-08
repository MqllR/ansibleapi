#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse

import json

def validate_request(request):
    """
    Get an HttpRequest object and check for global structure.
    Return a JsonResponse object if we got an error.
    """
    
    if not request.method == 'POST':
        raise TypeError('Bad method')

    # Is empty?
    if request.META['CONTENT_LENGTH'] == '':
        raise TypeError('Empty request')

    # API KEY
    if not 'HTTP_APIKEY' in request.META:
        raise TypeError('Error: HTTP_APIKEY is missing')


def validate_data(json_data, struct):
    """
    Get a json object and a dict and compare each other.
    Return a JsonResponse object if we got an error.
    """

    if len(json_data) != len(struct):
        raise TypeError('unexpected number of params')

    for k, v in struct.items():
        
        if not k in json_data:
            raise TypeError('%s is missing' % k)

        if type(json_data[k]) is not v:
            raise TypeError('%s bad formatted' % k)

def json_data(request):
    """
    Get an HttpRequest object and return a json object
    """

    try:
        json_data = json.loads(request.body)

    except Exception as e:
        raise TypeError(str(e))

    return json_data
