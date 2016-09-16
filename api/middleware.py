#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse

from api.extras.exceptions import AnsibleException

class SimpleMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        """
        Handle exception from extras.utils and send JSON response
        """

        if isinstance(exception, AnsibleException):

            if request.path == '/api/run/':
                return JsonResponse({
                        'status': 'false',
                        'message': str(exception)
                    }, status=exception.error)
