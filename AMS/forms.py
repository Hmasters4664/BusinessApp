from django.forms import ModelForm
from AMS.models import *
from user.models import User

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields= ['acquisition_date','asset_name','description','asset_type','asset_barcode','asset_serial_number'
            ,'asset_location','asset_status','asset_user','asset_department','purchase_value','residual_value'
            ,'life_expectancy']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields= ['city','province','country','building','floor','adress']

class ModificationForm(ModelForm):
    class Meta:
        model = Modification
        fields = '__all__'

