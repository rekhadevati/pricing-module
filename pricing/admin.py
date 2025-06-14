from django.contrib import admin
from .models import PricingConfig, TimeMultiplier, WaitingCharge, PricingConfigLog

admin.site.register(PricingConfig)
admin.site.register(TimeMultiplier)
admin.site.register(WaitingCharge)
admin.site.register(PricingConfigLog)
