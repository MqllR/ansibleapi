#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.playbook.play import Play

from api.extras.ansiblebase import AnsibleBase
from api.extras.utils import validate_data

from pprint import pprint

class AnsibleTasks(AnsibleBase):
    """
    Run tasks on hosts
    """

    def __init__(self, hosts, tasks):
        super(AnsibleTasks, self).__init__(hosts=hosts)

        for task in tasks:
            struct_action = {
                'action': dict,
            }
    
            validate_data(task, struct_action)
    
            struct_task = {
                'module': unicode,
                'args': dict,
            }
    
            validate_data(task['action'], struct_task)
    
        self.tasks = tasks


    def run(self):
        """
        run ansible tasks for hosts
        """

        play_source = dict(
            name = "Ansible Tasks",
            hosts = self.hosts,
            gather_facts = 'no',
            tasks = self.tasks,
        )

        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)
        
        # Load options (not yet implemented)
        self.setOptions()

        # Run tasks
        self._run(play=play)
