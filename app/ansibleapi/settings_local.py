#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# DB parameters
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        #'USER': 'ansibleapi',
        #'PASSWORD': 'mypassword',
        #'HOST': 'localhost',
        #'PORT': '3306',
    }
}

# Path to playbook
PLAYBOOK_PATH = os.getenv('APP_DIR', '/opt') + '/playbooks/'
