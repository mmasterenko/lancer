# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Car, Service, Spares, TechLiquids, GeneralInfo, News, Actions, Stuff, Diagnostic


class GeneralInfoAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (u'Общая информация', {
            'fields': ('main_phone', 'address', 'email', 'feedbackURL', 'footerText'),
            'classes': ('wide',)
        }),
        (u'Настройки СМС', {
            'fields': ('sms_phone', 'is_smsing', 'apikey'),
            'classes': ('wide',)
        }),
        (u'Настройки почты', {
            'fields': ('recipient', 'subject', 'sender'),
            'classes': ('wide',)
        }),
        (u'О компании', {
            'fields': ('workhours', 'phones', 'about'),
            'classes': ('wide',)
        }),
        (u'для SEO', {
            'fields': ('title', 'meta_keywords', 'meta_desc'),
            'classes': ('collapse', 'wide')
        })
    ]


class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('header', 'text', 'date')}),
        (u'для SEO', {
            'fields': ('title', 'meta_keywords', 'meta_desc', 'url'),
            'classes': ('collapse', 'wide')
        })
    ]
    list_display = ('header', 'date', 'url')


class CarAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'subtype', 'engine', 'transmission', 'id')
    list_filter = ('type', 'subtype', 'engine', 'transmission')
    fields = ('type', 'subtype', 'engine', 'transmission')
    ordering = ('type', '-subtype', '-engine', 'transmission')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'type', 'price', 'price_cons')
    list_filter = ('car__type', 'type')
    save_as = True
    filter_horizontal = ('techliq', 'spares')
    list_select_related = ('car',)
    search_fields = ('name',)
    fields = ('type', 'name', 'price', 'price_cons', 'car', 'spares', 'techliq', 'car_name')

    def save_model(self, request, obj, form, change):
        obj.car_name = obj.car.name
        obj.save()


class SparesAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__', 'number', 'price', 'service_type')
    list_display_links = ('__unicode__',)
    list_filter = ('service_type',)
    search_fields = ('name', 'number')
    fields = ('name', 'number', 'price', 'service_type')
    save_as = True


class TechLiquidsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    fields = ('name', 'price')
    search_fields = ('name',)
    save_as = True


class StuffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    save_as = True


class DiagnosticAdmin(admin.ModelAdmin):
    list_select_related = ('car',)
    save_as = True
    list_display = ('__unicode__', 'car')
    list_filter = ('car__type',)
    filter_horizontal = ('services',)

admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Spares, SparesAdmin)
admin.site.register(TechLiquids, TechLiquidsAdmin)
admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Actions)
admin.site.register(Stuff, StuffAdmin)
admin.site.register(Diagnostic, DiagnosticAdmin)

admin.site.site_header = u'Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Лансер Сервис'
