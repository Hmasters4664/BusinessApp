from django.conf.urls import url
from AMS import views
from AMS.views import addAsset, addLocation, main, editAsset,Login, LocationList,ApprovalList, BulkUpload, noficications

urlpatterns = [
    url('login', Login.as_view(), name='login'),
    url('assets', main.as_view(), name='main'),
    url('add', addAsset.as_view(), name='add'),
    url ('location',addLocation.as_view(),name='location'),
    url('search',views.Search,name='search'),
    url(r'^asset/(?P<pk>\d+)/',editAsset.as_view(),name='modify'),
    url('Llist', LocationList.as_view(), name='Llist'),
    url('pending', ApprovalList.as_view(), name='pending'),
    url('specialsearch',views.SpecialSearch,name='specialsearch'),
    url('logout',views.logout,name='logout'),
    url(r'^approve/(?P<pk>\d+)/',views.approve,name='approve'),
    url(r'^export/csv/$', views.to_csv, name='assets_to_csv'),
    url(r'^export/xlsx/$', views.to_xlsx, name='assets_to_xlsx'),
    url('notifications', views.noficications, name='notifications'),
    url(r'XLSupload', BulkUpload.as_view(), name='xls_Upload')
]