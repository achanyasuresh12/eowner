from django.conf.urls import url
from .views import user

app_name = 'users'

urlpatterns = [
    url(r'^$', user, name='user_forms')

]
