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
        raise TypeError('Test')
#        msg = 'Error: bad method'
#        return JsonResponse({
#               'status': 'false',
#               'message': msg,
#           }, status= 500)

    # Is empty?
    if request.META['CONTENT_LENGTH'] == '':
        msg = 'Error: missing body'
        return JsonResponse({
               'status': 'false',
               'message': msg,
           }, status=500)

    # API KEY
    if not 'HTTP_APIKEY' in request.META:
        msg = 'Error: HTTP_APIKEY is missing'
        return JsonResponse({
               'status': 'false',
               'message': msg,
           }, status=500)


def validate_data(json_data, struct):
    """
    Get a json object and a dict and compare each other.
    Return a JsonResponse object if we got an error.
    """

    if len(json_data) != len(struct):
        msg = 'Error: unexpected number of params' 
        return JsonResponse({
           'status': 'false',
           'message': msg,
        }, status=500)

    for k, v in struct.items():
        
        if not k in json_data:
            msg = 'Error: ' + k + ' is missing'
            return JsonResponse({
                    'status': 'false',
                    'message': msg,
                 }, status=500)

        print type(json_data[k]), v 
        if type(json_data[k]) is not v:
            msg = 'Error: ' + k + ' bad formatted'
            return JsonResponse({
                    'status': 'false',
                    'message': msg,
                }, status=500)

def json_data(request):
    """
    Get an HttpRequest object and return a json object
    """

    try:
        json_data = json.loads(request.body)

    except Exception as e:
        msg = 'Error: ' + str(e)
        return JsonResponse({
                   'status': 'false',
                   'message': msg,
               }, status=500)

    return json_data

