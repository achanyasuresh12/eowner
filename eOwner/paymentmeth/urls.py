from django.conf.urls import url
from .views import payments

app_name = 'paymentmeth'

urlpatterns = [
    url(r'^$', payments, name='payment'),
]
