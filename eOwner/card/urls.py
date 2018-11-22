from django.conf.urls import url
from .views import cards

app_name = 'card'

urlpatterns = [
    url(r'^$', cards, name='card'),
]
