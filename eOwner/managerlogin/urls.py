from django.conf.urls import url
from .views import mgrlogin, managerhome

app_name = 'managerlogin'

urlpatterns = [
    url(r'^$', mgrlogin, name='managerlogin_forms'),
    url(r'^managerhome$', managerhome, name='managerhome'),

]
