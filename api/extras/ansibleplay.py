#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.playbook import Playbook

from api.extras.ansiblebase import AnsibleBase

class AnsiblePlaybook(AnsibleBase):
    
    def __init__(self, hosts, playbook):
    	"""
    	Instanciate class with a dict of hosts and path to playbook file
   	"""
        super(AnsiblePlaybook, self).__init__(hosts=hosts)
        self.playbook = playbook

    def run(self):
    	"""
    	run ansible playbook for hosts
    	"""
        pb = Playbook.load(self.playbook, variable_manager=self.variable_manager, loader=self.loader)
        plays = pb.get_plays()
    
        self.setOptions()
        self.setInventory()

        for play in plays:
            self._run(play=play)
        #pb = PlaybookExecutor(playbooks=[self.playbook], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=password)
        #pb.run()
