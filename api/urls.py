from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'^run/$', run),
    url(r'^test/$', test),
]
