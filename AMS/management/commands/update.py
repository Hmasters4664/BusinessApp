from AMS.models import Asset
from django.core.management.base import BaseCommand
import datetime

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if Asset.objects.all().count()> 0:
            assets = Asset.objects.all()
            for asset in assets:
                thisyear = datetime.date.today().year
                buyyear = asset.acquisition_date.year
                if asset.depr_model == 'Straight Line':
                    asset.current_value=straight(thisyear,buyyear,asset.life_expectancy,asset.purchase_value,asset.residual_value)


def straight(thisy,buyY,life,value,salvagevalue):
    depreciatable_cost=value-salvagevalue
    depreciation_rate=depreciatable_cost/life
    current_val=depreciatable_cost-(thisy-buyY)*(depreciation_rate)
    print((thisy-buyY))
    return current_val

