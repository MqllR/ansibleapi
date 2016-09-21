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
