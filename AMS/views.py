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
from django.http import JsonResponse
from .forms import AssetForm, LocationForm, ModificationForm

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



class main(View):

    def get(self,request,*args,**kwargs):
        return render_to_response('index.html')

def Asset_asJson(request):
    object_list = Asset.objects.all().values()
    
    jason = list(object_list)
    test_all = json.dumps({"data": jason},indent=4, sort_keys=True, default=str)
    data = {'test_data': test_all,}
    
    return HttpResponse(test_all, content_type='application/json')



