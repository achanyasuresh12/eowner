from django.conf.urls import url
from .views import seatde

app_name = 'seatdetails'

urlpatterns = [
    url(r'^$', seatde, name='seatinform_forms'),

]
