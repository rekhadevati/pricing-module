from django.db import models
from django.contrib.auth.models import User

DAYS = [
    ("Mon", "Monday"),
    ("Tue", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thu", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday"),
]

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    days_active = models.JSONField(help_text="Days like ['Mon', 'Tue']")
    base_distance = models.FloatField(help_text="Base distance in KM")
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TimeMultiplier(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='time_multipliers')
    min_minutes = models.PositiveIntegerField()
    max_minutes = models.PositiveIntegerField()
    multiplier = models.FloatField()

    def __str__(self):
        return f"{self.min_minutes}-{self.max_minutes} min: {self.multiplier}x"

class WaitingCharge(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='waiting_charges')
    free_minutes = models.PositiveIntegerField(default=3)
    rate_per_3_min = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"After {self.free_minutes} mins: Rs. {self.rate_per_3_min}/3min"

class PricingConfigLog(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    action = models.CharField(max_length=20)
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.actor} at {self.timestamp}"
