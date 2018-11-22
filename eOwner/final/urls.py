from django.conf.urls import url
from .views import finals

app_name = 'final'

urlpatterns = [
    url(r'^$', finals, name='final'),
]
