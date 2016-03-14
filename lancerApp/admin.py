# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Car, Service, Spares, TechLiquids, GeneralInfo, News, Actions, Stuff, CarGroupOrder, Diagnostic


class GeneralInfoAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (u'Общая информация', {
            'fields': ('main_phone', 'email', 'address', 'footerText', 'feedbackURL'),
            'classes': ('wide',)
        }),
        (u'О компании', {
            'fields': ('workhours', 'phones', 'about'),
            'classes': ('wide', 'collapse')
        }),
        (u'Описания для машин', {
            'fields': ('car_lancer9', 'car_lancer10', 'car_evolution', 'car_lancerASX'),
            'classes': ('wide', 'collapse')
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


class CarGroupOrderAdmin(admin.ModelAdmin):
    list_display = ('type', 'order1', 'order2', 'order3')
    fieldsets = [(None, {
        'fields': ('type', 'order1', 'order2', 'order3'),
        'description': u'по умолчанию используется следующий порядок: 1.подвид 2.трансмиссия 3.двигатель'
    })]


class CarAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'subtype', 'engine', 'transmission', 'id')
    list_filter = ('type', 'subtype', 'engine', 'transmission')
    fields = ('type', 'subtype', 'engine', 'transmission')
    ordering = ('type', '-subtype', '-engine', 'transmission')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'type', 'price', 'price_cons')
    list_editable = ('car',)
    list_filter = ('car__type', 'car__subtype', 'car__engine', 'car__transmission', 'type')
    save_as = True
    filter_horizontal = ('techliq', 'spares')
    list_select_related = ('car',)
    search_fields = ('name',)
    fields = ('type', 'name', 'price', 'price_cons', 'car', 'spares', 'techliq')


class SparesAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'number', 'price', 'service_type', 'car')
    list_filter = ('car__type', 'service_type')
    search_fields = ('name', 'number')
    fieldsets = [
        (None, {'fields': ('name', 'number', 'price', 'service_type')}),
        (u'применимо только к данной модели', {'fields': ('car',), 'classes': ('collapse',)})
    ]
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
    save_as = True
    filter_horizontal = ('services',)

admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Spares, SparesAdmin)
admin.site.register(TechLiquids, TechLiquidsAdmin)
admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Actions)
admin.site.register(Stuff, StuffAdmin)
admin.site.register(CarGroupOrder, CarGroupOrderAdmin)
admin.site.register(Diagnostic, DiagnosticAdmin)

admin.site.site_header = u'Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Лансер Сервис'
