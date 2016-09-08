#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare(MiddlewareMixin):

    def process_exception(self, request, exception):
        """
        Handle exception from extras.utils and send JSON response
        """

        if request.path == '/api/run/':
            return JsonResponse({
                    'status': 'false',
                    'message': str(exception)
                }, status=500)
