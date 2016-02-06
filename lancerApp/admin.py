# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Car, Service, Spares, TechLiquids, GeneralInfo, News, Actions, Stuff


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


class CarAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'engine', 'transmission')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'type', 'price', 'price_cons')
    list_filter = ('car', 'type')
    save_as = True
    filter_horizontal = ('techliq', 'spares')


class SparesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'car')
    list_filter = ('car',)
    fieldsets = [
        (None, {'fields': ('name', 'price')}),
        (u'применимо только к данной модели', {'fields': ('car',), 'classes': ('collapse',)})
    ]
    save_as = True


class TechLiquidsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'car')
    list_filter = ('car',)
    fieldsets = [
        (None, {'fields': ('name', 'price')}),
        (u'применимо только к данной модели', {'fields': ('car',), 'classes': ('collapse',)})
    ]
    save_as = True


admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Spares, SparesAdmin)
admin.site.register(TechLiquids, TechLiquidsAdmin)
admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Actions)
admin.site.register(Stuff)

admin.site.site_header = u'Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Лансер Сервис'
