#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

from pprint import pprint

class AnsibleBase(object):
    """
    This class will extends for playing playbook and tasks!
    """
 
    def __init__(self, hosts):
        self.hosts = hosts
        self.variable_manager = VariableManager()
        self.loader = DataLoader()

    def setOptions(self, password={}, remote_user='root'):
        Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])

        self.options = Options(
                listtags=False,
                listtasks=False,
                listhosts=False,
                syntax=False,
                connection='ssh',
                module_path=None,
                forks=100,
                remote_user=remote_user,
                private_key_file=None,
                ssh_common_args=None,
                ssh_extra_args=None,
                sftp_extra_args=None,
                scp_extra_args=None,
                become=True,
                become_method=None,
                become_user='root',
                verbosity=None,
                check=False
            )

        self.password = password


    def getResult(self):
        """
        Build a the answer et return it as a Json object
        """

        result = {}

        if self.callback.host_ok:

            host_result = []

            for host in self.callback.host_ok:
                host_result.append({ host: self.callback.host_ok[host]._result})

            result['host_ok'] = host_result

        if self.callback.host_unreachable:

            host_result = []

            for host in self.callback.host_unreachable:
                host_result.append({ host: self.callback.host_unreachable[host]._result})

            result['host_unreachable'] = host_result

        if self.callback.host_failed:

            host_result = []

            for host in self.callback.host_failed:
                host_result.append({ host: self.callback.host_failed[host]._result})

            result['host_failed'] = host_result

        return result


    def _run(self, play):
        """
        run a tasksqueue manager
        """

        self.inventory = Inventory(loader=self.loader, variable_manager=self.variable_manager, host_list=self.hosts)
        self.variable_manager.set_inventory(self.inventory)
        
        tqm = None
        self.callback = ResultsCollector()

        try:
            tqm = TaskQueueManager(
                    inventory=self.inventory,
                    variable_manager=self.variable_manager,
                    loader=self.loader,
                    options=self.options,
                    passwords=self.password,
                )
            tqm._stdout_callback = self.callback
            self.result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()


class ResultsCollector(CallbackBase):
    """
    Class to capture output
    """

    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.host_ok     = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result,  *args, **kwargs):
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result,  *args, **kwargs):
        self.host_failed[result._host.get_name()] = result
