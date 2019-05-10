from django.conf.urls import url
from AMS import views
from AMS.views import addAsset, addLocation, main

urlpatterns = [
    url('assets', main.as_view(), name='main'),
    url('add', addAsset.as_view(), name='add'),
    url ('location',addLocation.as_view(),name='location'),
    url(r'^/api/search/',views.Search,name='search'),
]