#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory

from collections import namedtuple

class AnsiblePlaybook(object):
    

    def __init__(self, hosts, playbook):
    	"""
    	Instanciate class with a dict of hosts and path to playbook file
   	"""
        self.hosts = hosts

        # TODO CREATE A FUNCTION IN UTILS TO CHECK playbook
        try:
            with open(playbook) as infile:
                self.playbook = playbook
        except IOError as e:
            print e


    def run(self):
    	"""
    	run ansible playbook for hosts
    	"""
    	loader              = DataLoader()
    	variable_manager    = VariableManager()
    	password            = {}

        inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=self.hosts)
        Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
        options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='root', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)

        pb = PlaybookExecutor(playbooks=[self.playbook], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=password)

        pb.run()
