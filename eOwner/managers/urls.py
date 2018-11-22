from django.conf.urls import url
from .views import manager

app_name = 'managers'

urlpatterns = [
    url(r'^$', manager, name='manager_forms')
]
