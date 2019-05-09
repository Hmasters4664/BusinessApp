from django.conf.urls import url
from AMS import views
from AMS.views import addAsset, addLocation, main, AssetListJson

urlpatterns = [
    url('assets', main.as_view(), name='main'),
    url('add', addAsset.as_view(), name='add'),
    url ('location',addLocation.as_view(),name='location'),
    url('set',views.Asset_asJson,name='getsets'),
    url(r'^asset_data/$', AssetListJson.as_view(), name="asset_list"),
]