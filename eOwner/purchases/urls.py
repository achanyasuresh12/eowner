from django.conf.urls import url
from .views import purchase

app_name = 'purchases'

urlpatterns = [
    url(r'^$', purchase, name='purchases_forms'),
]
