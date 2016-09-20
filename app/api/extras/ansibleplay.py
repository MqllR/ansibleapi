#!/usr/bin/python
# -*- coding: utf-8 -*-

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
