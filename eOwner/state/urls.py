from django.conf.urls import url
from .views import state, edit_state, delete_state

app_name = 'state'

urlpatterns = [
    url(r'^$', state, name='state_forms'),
    url(r'^edit_state/(?P<pk>\d+)/$', edit_state, name='edit_state'),
    url(r'^delete_state/(?P<pk>\d+)/$', delete_state, name='delete_state'),
]
