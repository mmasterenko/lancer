from django.contrib import admin
from .models import Car, Service, Spares, TechLiquids


class CarAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'engine', 'transmission')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'car', 'price', 'price_cons')


class SparesAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'price')


class TechLiquidsAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'amount', 'price')


admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Spares, SparesAdmin)
admin.site.register(TechLiquids, TechLiquidsAdmin)
