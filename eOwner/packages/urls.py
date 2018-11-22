from django.conf.urls import url
from .views import packg, edit_packg, delete_packg

app_name = 'packages'

urlpatterns = [
    url(r'^$', packg, name='packages_forms'),
    url(r'^edit_packg/(?P<pk>\d+)/$', edit_packg, name='edit_packg'),
    url(r'^delete_packg/(?P<pk>\d+)/$', delete_packg, name='delete_packg'),
]
