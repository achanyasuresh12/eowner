from django.conf.urls import url
from .views import purchasesdetails

app_name = 'purchasesdet'

urlpatterns = [
    url(r'^$', purchasesdetails, name='purchasesdetails_forms'),
    # url(r'^(?P<pk>\d+)$', purchasedetails, name='purchasedetails_forms'),
]
