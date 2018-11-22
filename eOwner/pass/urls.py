from django.conf.urls import url
from .views import passhome

app_name = 'pass'

urlpatterns = [
    url(r'^$', passhome, name='pass_forms'),

]
