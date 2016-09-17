#!/usr/bin/env python
# -*- coding: utf-8 -*

from api.models import User, Host

from api.extras.exceptions import AnsibleException

class AnsibleAuth(object):

    def __init__(self, apikey):

        if self._apikeyexist(apikey):
            self.apikey = apikey

    def isauthorized(self, host):

        if host in self._gethosts():
            return True
        else:
            return False

    def _gethosts(self):
        user = User.objects.filter(apikey=self.apikey)
        hosts = Host.objects.filter(user__in=user)

        myhost = []

        for host in hosts:
            myhost.append(host.host)

        myhost
        return myhost

    def _apikeyexist(self, apikey):

        if User.objects.filter(apikey=apikey):
            return True
        else:
            raise AnsibleException('APIKEY does not exist', error=401)
