# properties/admin.py
from django.contrib import admin
from .models import Address, Property, Unit, Tenant, Lease, Payment, MaintenanceTicket

admin.site.register(Address)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(Payment)
admin.site.register(MaintenanceTicket)
