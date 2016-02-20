# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Customer, Visit, CustomUser


class VisitInline(admin.StackedInline):
    model = Visit
    extra = 0
    can_delete = True
    show_change_link = True
    filter_horizontal = ('services',)


class CustomerAdmin(admin.ModelAdmin):
    # inlines = [VisitInline]
    search_fields = ('car_number', 'surname', 'name', 'patronymic', 'note')
    list_filter = ('car',)
    list_display = ('get_abbrev_name', 'phone', 'get_car_number', 'car', 'get_visit_count', 'get_last_visit')
    list_select_related = ('car',)

    fieldsets = [
        (
            u'информация о машине',
            {
                'fields': ('car_number', 'car'),
                'classes': ('wide',)
            },
        ),
        (
            u'информация о клиенте',
            {
                'fields': ('surname', 'name', 'patronymic', 'phone')
            },
        ),
        (
            u'дополнительная информация',
            {
                'fields': ('note',)
            },
        ),
        (
            u'пароль',
            {
                'fields': ('password',),
                'classes': ('collapse',)
            },
        )
    ]


class VisitAdmin(admin.ModelAdmin):
    ordering = ('-date', '-id')
    date_hierarchy = 'date'
    search_fields = ('customer__name', 'customer__surname', 'customer__patronymic')
    list_filter = ('customer__car',)
    list_display = ('get_visit_number', 'date', 'get_customer_car', 'get_sum')
    list_select_related = ('customer',)

    fieldsets = [
        (None, {
            'fields': (('date', 'km'), 'customer', 'services', 'note'),
        })
    ]
    filter_horizontal = ('services',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(CustomUser)
