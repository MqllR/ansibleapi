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


class AnsibleException(Exception):
    """
    A custom Exception to return a json object (middleware)
    """

    def __init__(self, msg, error=500):
        super(AnsibleException, self).__init__(msg)

        self.error = error
