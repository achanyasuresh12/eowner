from django.conf.urls import url
from .views import businf, edit_businfo, delete_businfo

app_name = 'businfo'

urlpatterns = [
    url(r'^$', businf, name='businfo_forms'),
    url(r'^edit_businfo/(?P<pk>\d+)/$', edit_businfo, name='edit_businfo'),
    url(r'^delete_businfo/(?P<pk>\d+)/$', delete_businfo, name='delete_businfo'),
]
