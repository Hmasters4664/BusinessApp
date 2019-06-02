# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Asset, Location, Modification
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import View, TemplateView
from django.core import serializers
import json
from .forms import AssetForm, LocationForm, ModificationForm
from django.views.generic.list import ListView
from django.views.generic import UpdateView
#from .background import hello
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
class addAsset(LoginRequiredMixin, FormView):
    model= Asset
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    template_name= 'assets.html'
    form_class = AssetForm
    success_url = '/assetmanager/assets/'
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class addLocation(LoginRequiredMixin, FormView):
    model=Location
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    template_name= 'addlocation.html'
    form_class = LocationForm
    success_url = '/assetmanager/assets/'
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)



class main(LoginRequiredMixin, ListView):
    model = Asset
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    #hello()
    template_name= 'index.html'
    context_object_name = 'assets'
    paginate_by = 10
    queryset = Asset.objects.all()

@login_required
def Search(request):
    object_list = Asset.objects.filter(asset_name__startswith=request.GET.get('search')).values("asset_id","acquisition_date",
                                                                                              "asset_name","description","asset_type","asset_barcode","asset_serial_number",
                                                                                              "asset_location","asset_status","asset_owner")
    
    jason = list(object_list)
    return JsonResponse(jason, safe=False)

class editAsset(LoginRequiredMixin, UpdateView):
    model = Asset
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'assets.html'
    form_class = AssetForm
    success_url = '/assetmanager/assets/'

    def get_object(self, *args, **kwargs):
        asset = get_object_or_404(Asset, pk=self.kwargs['pk'])
        date = datetime.now()
        dates=date.strftime("%Y-%m-%d")
        asset.modified_date = dates
        return asset


class Login(FormView):
    template_name = 'login.html'
    success_url = '/assetmanager/assets/'

