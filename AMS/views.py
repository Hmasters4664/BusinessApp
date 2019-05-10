# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Asset, Location, Modification
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import View, TemplateView
from django.core import serializers
import json
from .forms import AssetForm, LocationForm, ModificationForm
from django.views.generic.list import ListView


# Create your views here.
class addAsset(FormView):
    model= Asset
    template_name= 'assets.html'
    form_class = AssetForm
    success_url = '/weblog/assets/'
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class addLocation(FormView):
    model=Location
    template_name= 'addlocation.html'
    form_class = LocationForm
    success_url = '/weblog/assets/'
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)



class main(ListView):
    model = Asset
    template_name= 'index.html'
    context_object_name = 'assets'
    paginate_by = 10
    queryset = Asset.objects.all()

def Search(request):
    object_list = Asset.objects.filter(asset_name__startswith=request.GET.get('search'))
    
    #jason = list(object_list)
    test_all = json.dumps(object_list)

    return HttpResponse(test_all, content_type='application/json')




