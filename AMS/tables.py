from table import Table
from table.columns import Column
from .models import Asset, Location, Modification

class AssetTable(Table):
    id = Column(field='asset_id')
    name = Column(field='asset_name')
    date = Column(field='acquisition_date')
    description = Column(field='description')
    type = Column(field='asset_type')
    barcode = Column(field='asset_barcode')
    serial_number = Column(field='asset_serial_number')
    location = Column(field='asset_location')
    status = Column(field='asset_status')
    owner = Column(field='asset_owner')
    department = Column(field='asset_department')
    added_date = Column(field='added_date')
    modified_date = Column(field='modified_date')

    class Meta:
        model = Asset
        ajax = True

