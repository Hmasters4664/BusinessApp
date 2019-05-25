# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Asset(models.Model):
    
    ASSET_CHOICES = (
            ('Automobile',   'Automobile'),
            ('AV Equipment', 'AV Equipment'),
            ('Computer Equipment',  'Computer Equipment'),
            ('Office Furniture & Stationary', 'Office Furniture & Stationary'),
        )
    STATUS_CHOICES = (
            ('Working', 'Working'),
            ('Disabled', 'Disabled'),
    )

    Depreciation = (
        ('Straight Line', 'Straight Line'),
        ('Double-Declining Balance', 'Double-Declining Balance'),
        ('Sum of Years', 'Sum of Years'),
    )
    asset_id= models.AutoField(primary_key=True)
    acquisition_date = models.DateField(default=datetime.date.today)
    asset_name =  models.CharField(max_length=50, blank=True, )
    description = models.TextField(max_length=2000)
    asset_type = models.CharField(choices=ASSET_CHOICES, max_length=30)
    asset_barcode = models.CharField(max_length=30, blank=True, )
    asset_serial_number = models.CharField(max_length=80, blank=True, )
    asset_location = models.ForeignKey("Location", on_delete=models.PROTECT)
    asset_status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    asset_owner = models.CharField(max_length=50)
    asset_department = models.CharField(max_length=50)
    added_date = models.DateField(default=datetime.date.today)
    modified_date = models.DateField(default=datetime.date.today)
    purchase_value = models.DecimalField(max_digits=19, decimal_places=2,default=200.00)
    residual_value = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)
    current_value = models.DecimalField(max_digits=19, decimal_places=2, default=200.00)
    life_expectancy = models.IntegerField(default=3)
    depr_model = models.CharField(choices=Depreciation, max_length=30,default='Straight Line')
    currentVal_date = models.DateField(default=datetime.date.today)
    #invoices = models.FileField(upload_to='invoices/', blank=True, )

    def natural_key(self):
        return self.my_natural_key




class Location(models.Model):
    location_id= models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    building = models.TextField(max_length=1000, blank=True)
    floor =models.CharField(max_length=3)
    adress = models.TextField(max_length=200)

    def __str__(self):
        return self.adress


class Modification(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    asset = models.ForeignKey("Asset", on_delete=models.PROTECT)
    modified_date = models.DateField()
    description = models.TextField(max_length=1000)


    