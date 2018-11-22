from django.conf.urls import url
from .views import report

app_name = 'viewdailyreport'

urlpatterns = [
    url(r'^$', report, name='viewdailyreport_forms'),
]
