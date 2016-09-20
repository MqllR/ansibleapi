#!/usr/bin/python
# -*- coding: utf-8 -*-

class AnsibleException(Exception):
    """
    A custom Exception to return a json object (middleware)
    """

    def __init__(self, msg, error=500):
        super(AnsibleException, self).__init__(msg)

        self.error = error
