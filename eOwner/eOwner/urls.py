"""eOwner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^passengers/', include('users.urls')),
    url(r'^passengerlogin/', include('userlogin.urls')),
    url(r'^managerlogin/', include('managerlogin.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^complaint/', include('complaint.urls')),
    url(r'^busdetails/', include('busdetails.urls')),
    url(r'^dailyreport/', include('dailyrepo.urls')),
    url(r'^seatbooking/', include('booking.urls')),
    url(r'^packages/', include('packages.urls')),
    url(r'^state/', include('state.urls')),
    #url(r'^district/', include('district.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^managers/', include('managers.urls')),
    url(r'^businfo/', include('businfo.urls')),
    url(r'^bookbus/', include('bookbus.urls')),
    url(r'^purchase/', include('purchases.urls')),
    url(r'^purchasedet/', include('purchasesdet.urls')),
    url(r'^viewcomplaint/', include('viewcomplaint.urls')),
    url(r'^viewbusdet/', include('viewbusdet.urls')),
    url(r'^viewbfeedback/', include('viewfeedback.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^viewdailyreport/', include('viewdailyreport.urls')),
    url(r'^viewbus/', include('viewbus.urls')),
    url(r'^pass/', include('pass.urls')),
    url(r'^managerlogout/', include('managerlogout.urls')),
    url(r'^adminlogout/', include('adminlogout.urls')),
    url(r'^seatdetails/', include('seatdetails.urls')),
    url(r'^viewseatdetails/', include('viewseatdetails.urls')),
    url(r'^custdetails/', include('custdetails.urls')),
    url(r'^adminviewbus/', include('adviewbus.urls')),
    url(r'^eowner/', include('menu.urls')),
    url(r'^card/', include('card.urls')),
    url(r'^net/', include('net.urls')),
    url(r'^final/', include('final.urls')),
    url(r'^payment/', include('paymentmeth.urls')),
    url(r'^employes/', include('employe.urls')),
    url(r'^$', include('menu.urls')),







]
