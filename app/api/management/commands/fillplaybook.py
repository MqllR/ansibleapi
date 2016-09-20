#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
#from os import walk

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import Playbook

RE_PLAYBOOK = re.compile(r'^\S+\.yml$')

class Command(BaseCommand):

    help = 'Fill DB with playbooks'

    def handle(self, *args, **options):

        # We get all entry in Playbook table
        pb_indb = []

        pb = Playbook.objects.all()
        for pb_file in pb:
            pb_indb.append(pb_file.playbook)

        # And playbook in FS
        file_path = []

        for root, directories, files in os.walk(settings.PLAYBOOK_PATH):
            for filename in files:
                full_path =  os.path.join(root, filename)

                if RE_PLAYBOOK.match(full_path):
                    file_path.append(full_path.split(settings.PLAYBOOK_PATH)[1])

        # Compare playbooks in FS and DB
        for pb in file_path:
            if pb not in pb_indb:
                Playbook(playbook=pb).save()
                self.stdout.write(self.style.SUCCESS("{0:<40} {1:>8}".format(pb, 'added')))
            else:
                self.stdout.write("{0:<40} {1:>8}".format(pb, 'skipped'))

        for pb in pb_indb:
            if not os.path.isfile(settings.PLAYBOOK_PATH + pb):
                Playbook.objects.filter(playbook=pb).delete()
                self.stdout.write(self.style.NOTICE("{0:<40} {1:>8}".format(pb, 'delete')))
