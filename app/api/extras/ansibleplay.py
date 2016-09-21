#!/usr/bin/python
# -*- coding: utf-8 -*-

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


from os.path import isfile

from ansible.playbook import Playbook

from api.extras.ansiblebase import AnsibleBase
from api.extras.exceptions import AnsibleException

from django.conf import settings

class AnsiblePlaybook(AnsibleBase):
    
    def __init__(self, hosts, playbook):
    	"""
    	Instanciate class with a dict of hosts and path to playbook file
   	"""
        super(AnsiblePlaybook, self).__init__(hosts=hosts)

        from api.models import Playbook

        if Playbook.objects.filter(playbook=playbook):
            self.playbook = playbook
        else:
            raise AnsibleException('%s does not exist' % playbook)

    def run(self):
    	"""
    	run ansible playbook for hosts
    	"""
        pb = Playbook.load(settings.PLAYBOOK_PATH + self.playbook, variable_manager=self.variable_manager, loader=self.loader)
        plays = pb.get_plays()
    
        self.setOptions()
        #self.setInventory()

        for play in plays:
            self._run(play=play)
