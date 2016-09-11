from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'^run/$', run_playbook),
    url(r'^test/$', test),
]
