from rest_framework import serializers
from AMS.models import Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('acquisition_date', 'asset_name', 'description', 'asset_type', 'asset_barcode', 'asset_serial_number'
            , 'asset_location', 'asset_status', 'asset_user', 'asset_department', 'purchase_value', 'residual_value'
            , 'life_expectancy')

