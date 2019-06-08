from AMS.models import Asset
from django.core.management.base import BaseCommand
import datetime
from decimal import *

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if Asset.objects.all().count()> 0:
            assets = Asset.objects.all()
            for asset in assets:
                thisyear = datetime.date.today().year
                buyyear = asset.acquisition_date.year
                diff = datetime.date.today() - asset.acquisition_date
                days = diff.days
                if asset.depr_model == 'Straight Line':
                    asset.current_value=straight_d(days,asset.life_expectancy,asset.purchase_value,asset.residual_value)
                    asset.currentVal_date = datetime.date.today()
                    asset.save()

                if asset.depr_model == 'Double-Declining Balance':
                    cur_val=declining_balence_d(days,asset.life_expectancy,asset.current_value)
                    asset.currentVal_date = datetime.date.today()
                    asset.current_value=cur_val
                    asset.save()


#straight line depreciation per day

def straight_d(days,life,value,salvagevalue):
    depreciatable_cost=value-salvagevalue
    depreciation_rate=depreciatable_cost/(life*365)
    current_val=depreciatable_cost-(days)*(depreciation_rate)
    print((current_val))
    print((days))
    return current_val

#double declining balence (ask patty)

def declining_balence_d(days,life,value):
    depreciationrate = (Decimal(1) / Decimal(365 * life)) * 2
    print(depreciationrate)
    current_val = value
    for x in range(1, 366):
        minus = (depreciationrate * current_val)
        current_val = current_val - minus
        print(x)
        print(value - current_val)

    print((current_val))
    return current_val