#!/usr/bin/env python
# -*- coding: utf-8 -*

################################################################################
#    Ansible API is a Rest API to run ansible playbooks and tasks
#    Copyright (C) <2016>  <Mael Regnery>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################


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

    def getusername(self):
        user = User.objects.get(apikey=self.apikey)
        return user.user

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
