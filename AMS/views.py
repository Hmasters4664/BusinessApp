# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.http import is_safe_url
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
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout


# Create your views here.
class addAsset(LoginRequiredMixin, FormView):
    model= Asset
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    template_name= 'assets.html'
    form_class = AssetForm
    success_url = '/assetmanager/assets/'
    def form_valid(self,form):
        asset=form.save(commit=False)
        asset.asset_owner=self.request.user
        asset.save()
        return super().form_valid(form)
########################################################################################################################
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

#######################################################################################################################

class main(LoginRequiredMixin, ListView):
    model = Asset
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    #hello()
    template_name= 'index.html'
    context_object_name = 'assets'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_manager:
            return Asset.objects.all()
        else:
            return Asset.objects.filter(asset_owner=self.request.user)
########################################################################################################################
@login_required
def Search(request):
    object_list = Asset.objects.filter(asset_name__startswith=request.GET.get('search')).values("asset_id",
                                                     "acquisition_date", "asset_name",
                                                     "description", "asset_type", "asset_barcode",
                                                     "asset_serial_number",
                                                     "asset_location", "asset_status", "asset_owner")

    jason = list(object_list)
    return JsonResponse(jason, safe=False)

########################################################################################################################
@login_required
def approve(request):
    if request.user.is_manager:
        asset = get_object_or_404(Asset, pk=request.kwargs['pk'])
        asset.is_approved=True
        asset.save()
        return redirect('approvallist')

    else:
        return HttpResponseForbidden()



    
#######################################################################################################################

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
        asset.asset_department = self.request.user.department
        return asset

########################################################################################################################
class Login(FormView):
    template_name = 'login.html'
    success_url = '/assetmanager/assets/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(Login, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to
#########################################################################################################################
class LocationList(LoginRequiredMixin, ListView):
    model = Location
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    #hello()
    template_name= 'location.html'
    context_object_name = 'locations'
    paginate_by = 10
    queryset = Location.objects.all()

########################################################################################################################
class ApprovalList(LoginRequiredMixin, ListView):
    model = Asset
    login_url = '/assetmanager/login/'
    redirect_field_name = 'redirect_to'
    #hello()
    template_name= 'approval_page.html'
    context_object_name = 'assets'
    paginate_by = 10
    queryset = Asset.objects.filter(asset_is_approved=False)

########################################################################################################################
@login_required
def SpecialSearch(request):
    object_list = Asset.objects.filter(asset_name__startswith=request.GET.get('search')).filter(asset_is_approved=False).values("asset_id",
                                                     "acquisition_date", "asset_name",
                                                     "description", "asset_type", "asset_barcode",
                                                     "asset_serial_number",
                                                     "asset_location", "asset_status", "asset_owner")

    jason = list(object_list)
    return JsonResponse(jason, safe=False)