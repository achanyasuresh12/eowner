from django.conf.urls import url
from .views import adlogout

app_name = 'adminlogout'

urlpatterns = [
    url(r'^$', adlogout, name='adminlogout_forms'),
]
