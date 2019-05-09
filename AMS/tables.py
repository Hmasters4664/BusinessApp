import django_tables2 as tables
from .models import Asset, Location, Modification

class AssetTable(tables.Table):
    class Meta:
        model = Asset
        template_name = 'django_tables2/bootstrap.html'
