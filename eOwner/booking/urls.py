from django.conf.urls import url
from .views import book, edit_book, delete_book

app_name = 'booking'

urlpatterns = [
    url(r'^$', book, name='booking_forms'),
    url(r'^edit_book/(?P<pk>\d+)/$', edit_book, name='edit_book'),
    url(r'^delete_book/(?P<pk>\d+)/$', delete_book, name='delete_book'),
]
