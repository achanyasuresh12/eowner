from django.conf.urls import url
from .views import mglogout

app_name = 'managerlogout'

urlpatterns = [
    url(r'^$', mglogout, name='managerlogout_forms'),
]
