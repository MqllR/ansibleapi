from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'^run/playbook/$', run_playbook),
    url(r'^run/tasks/$', run_tasks),
]
