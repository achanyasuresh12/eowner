from django.conf.urls import url
from .views import menus

app_name = 'menu'

urlpatterns = [
    url(r'^$', menus, name='menu_forms'),
]
