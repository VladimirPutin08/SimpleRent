# models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Address(models.Model):
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, default="Dubai")
    postcode = models.CharField(max_length=20, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.line1}, {self.city}"

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    units = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=50, default="Unit")
    bedrooms = models.IntegerField(default=1)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_vacant = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.property.title} - {self.name}"

class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    id_document = models.FileField(upload_to='ids/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Lease(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='leases')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Lease {self.unit} {self.tenant}"

class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(default=timezone.now)
    provider_payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=32, default='completed')

    def __str__(self):
        return f"Payment {self.amount} for {self.lease}"

class MaintenanceTicket(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    status = models.CharField(max_length=20, default='open')
    created_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.unit} - {self.status}"
