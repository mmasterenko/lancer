# -*- coding: utf-8 -*-

from django.contrib.admin import helpers
from django.contrib.admin.exceptions import DisallowedModelAdminToField
from django.core.exceptions import PermissionDenied
from django.forms.formsets import all_valid
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _

from django.contrib import admin
from .models import Visit, CustomUser


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
            'fields': (('date', 'km'), 'customer', 'services', 'spares', 'techliqs', 'note'),
        })
    ]
    filter_horizontal = ('services', 'spares', 'techliqs')


class CustomUserAdmin(admin.ModelAdmin):
    # inlines = [VisitInline]
    search_fields = ('car_number', 'last_name', 'first_name', 'patronymic_name', 'note')
    list_filter = ('car__type',)
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
                'fields': ('last_name', 'first_name', 'patronymic_name', 'phone', 'email')
            },
        ),
        (
            u'дополнительная информация',
            {
                'fields': ('note',)
            },
        ),
    ]

    def add_view(self, request, form_url='', extra_context=None):

        saved_fieldsets = self.fieldsets
        self.fieldsets = None
        self.fields = ('car_number', 'password', 'car', 'last_name', 'first_name', 'patronymic_name', 'phone', 'email', 'note')

        IS_POPUP_VAR = '_popup'
        TO_FIELD_VAR = '_to_field'

        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        if to_field and not self.to_field_allowed(request, to_field):
            raise DisallowedModelAdminToField("The field %s cannot be referenced." % to_field)

        model = self.model
        opts = model._meta
        object_id = None
        add = object_id is None

        if not self.has_add_permission(request):
            raise PermissionDenied
        obj = None

        ModelForm = self.get_form(request, obj)
        if request.method == 'POST':
            form = ModelForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form_validated = True
                new_object = self.save_form(request, form, change=not add)
            else:
                form_validated = False
                new_object = form.instance
            formsets, inline_instances = self._create_formsets(request, new_object, change=not add)
            if all_valid(formsets) and form_validated:
                raw_password = new_object.password
                new_object.set_password(raw_password)
                self.save_model(request, new_object, form, not add)  # запись в базу
                self.save_related(request, form, formsets, not add)
                if add:
                    self.log_addition(request, new_object)
                    return self.response_add(request, new_object)
                else:
                    change_message = self.construct_change_message(request, form, formsets)
                    self.log_change(request, new_object, change_message)
                    return self.response_change(request, new_object)
        else:
            if add:
                initial = self.get_changeform_initial_data(request)
                form = ModelForm(initial=initial)
                formsets, inline_instances = self._create_formsets(request, self.model(), change=False)
            else:
                form = ModelForm(instance=obj)
                formsets, inline_instances = self._create_formsets(request, obj, change=True)

        adminForm = helpers.AdminForm(
            form,
            list(self.get_fieldsets(request, obj)),
            self.get_prepopulated_fields(request, obj),
            self.get_readonly_fields(request, obj),
            model_admin=self)
        media = self.media + adminForm.media

        inline_formsets = self.get_inline_formsets(request, formsets, inline_instances, obj)
        for inline_formset in inline_formsets:
            media = media + inline_formset.media

        context = dict(self.admin_site.each_context(request),
            title=(_('Add %s') if add else _('Change %s')) % force_text(opts.verbose_name),
            adminform=adminForm,
            object_id=object_id,
            original=obj,
            is_popup=(IS_POPUP_VAR in request.POST or
                      IS_POPUP_VAR in request.GET),
            to_field=to_field,
            media=media,
            inline_admin_formsets=inline_formsets,
            errors=helpers.AdminErrorList(form, formsets),
            preserved_filters=self.get_preserved_filters(request),
        )

        context.update(extra_context or {})

        self.fieldsets = saved_fieldsets
        self.fields = None

        return self.render_change_form(request, context, add=add, change=not add, obj=obj, form_url=form_url)


admin.site.register(Visit, VisitAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
