from django.contrib import admin
from .models import Car, Service, Spares, TechLiquids


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'car', 'price', 'price_cons')


class SparesAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_type', 'price')


class TechLiquidsAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_type', 'amount', 'price')


admin.site.register(Car)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Spares, SparesAdmin)
admin.site.register(TechLiquids, TechLiquidsAdmin)
