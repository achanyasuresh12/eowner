from django.conf.urls import url
from .views import emp

app_name = 'employe'

urlpatterns = [
    url(r'^$', emp, name='emp_forms')
]
