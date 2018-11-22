from django.conf.urls import url
from .views import bookbus

app_name = 'bookbus'

urlpatterns = [
    url(r'^$', bookbus, name='bookbus_forms'),

]
