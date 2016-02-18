# -*- coding: utf-8 -*-

from django.db import models
from lancerApp.models import Car, Service
from django.utils.timezone import now


class Customer(models.Model):
    class Meta:
        verbose_name = u'клиент'
        verbose_name_plural = u'клиенты'

    def __unicode__(self):
        return self.get_abbrev_name_car()

    @property
    def full_name(self):
        return u'%s %s %s' % (self.surname.title(),
                              self.name.title() if self.name else u'',
                              self.patronymic.title() if self.patronymic else u'')

    def get_abbrev_name(self):
        return u'%s %s. %s.' % (self.surname.title(),
                                self.name[0].upper() if self.name else u'',
                                self.patronymic[0].upper() if self.patronymic else u'')
    get_abbrev_name.short_description = u'ФИО'

    def get_abbrev_name_car(self):
        return u'%s (%s)' % (self.get_abbrev_name(), self.car)
    get_abbrev_name_car.short_description = u'ФИО + машина'

    def get_visit_count(self):
        return self.visit_set.count()
    get_visit_count.short_description = u'кол-во посещений'

    def get_car_number(self):
        return u'%s' % (self.car_number.upper())
    get_car_number.short_description = u'гос. номер'

    def get_last_visit(self):
        last_visit = self.visit_set.order_by('-date', '-id').first()
        if last_visit:
            return last_visit.date
    get_last_visit.short_description = u'последнее посещение'

    car_number = models.CharField(u'гос. номер авто (логин)', max_length=9)
    password = models.CharField(u'пароль', max_length=128)
    surname = models.CharField(u'фамилия', max_length=20)
    name = models.CharField(u'имя', max_length=20, blank=True, null=True)
    patronymic = models.CharField(u'отчество', max_length=20, blank=True, null=True)
    note = models.TextField(u'доп.инфо', blank=True, null=True)
    car = models.ForeignKey(Car, verbose_name=u'автомобиль', blank=True, null=True)
    phone = models.CharField(u'телефон', max_length=20, blank=True, null=True)


class Visit(models.Model):
    class Meta:
        verbose_name = u'посещение'
        verbose_name_plural = u'посещения'
        ordering = ('-date', '-id')

    def __unicode__(self):
        return self.date_customer_car

    @property
    def date_customer_car(self):
        return u'%s %s %s' % (self.date, self.customer.full_name, self.customer.car)

    def get_customer_car(self):
        return u'%s (%s)' % (self.customer.get_abbrev_name(), self.customer.car)
    get_customer_car.short_description = u'клиент'

    def get_visit_number(self):
        return self.id
    get_visit_number.short_description = u'Номер посещения'

    def get_sum(self):
        return u'%d руб' % sum([d.get('price') for d in self.services.values('price')])
    get_sum.short_description = u'стоимость работ'

    date = models.DateField(u'дата', default=now)
    km = models.PositiveIntegerField(u'пробег', blank=True, null=True)
    customer = models.ForeignKey(Customer, verbose_name=u'клиент')
    services = models.ManyToManyField(Service, verbose_name=u'оказанные услуги', blank=True)
    note = models.TextField(u'доп.инфо', blank=True, null=True)

