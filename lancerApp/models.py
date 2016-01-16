# -*- coding: utf-8 -*-

from django.db import models


CAR_TYPE = (
    ('lancer9', 'Lancer 9'),
    ('lancer10', 'Lancer 10'),
    ('evo', 'Evolution 6-10'),
    ('asx', 'Lancer ASX'),
    ('all', 'Все'),
)

SERVICE_TYPE = (
    ('oil',       'Замена жидкостей'),
    ('wheel',     'Рулевое управление'),
    ('brake',     'Тормозная система'),
    ('chassis',   'Ходовая часть'),
    ('engine',    'Двигатель'),
    ('transmiss', 'Трансмиссия'),
    ('electro',   'Электрика'),
    ('other',   'Другое'),
)


class Car(models.Model):
    class Meta:
        verbose_name_plural = u'машины'
        verbose_name = u'машина'
        unique_together = ('type', 'engine', 'transmission')

    TRANSMISSION_CHOICES = (
        ('auto', u'автомат'),
        ('mech', u'механика'),
        ('all',  u'любая'),
    )

    CAPACITY_CHOICES = (
        ('1.4', u'1.4'),
        ('1.6', u'1.6'),
        ('1.8', u'1.8'),
        ('2.0', u'2.0'),
        ('all', u'любой'),
    )

    def __unicode__(self):
        return '%s %s %s' % (self.get_type_display(), self.get_transmission_display(), self.engine)
    type = models.CharField(u'модель', max_length=20, choices=CAR_TYPE)
    engine = models.CharField(u'объем двигателя', max_length=4, choices=CAPACITY_CHOICES)
    transmission = models.CharField(u'коробка передач', max_length=4, choices=TRANSMISSION_CHOICES)


class Spares(models.Model):
    class Meta:
        verbose_name_plural = u'запчасти'
        verbose_name = u'запчасть'
        unique_together = ('name', 'car_type')

    def __unicode__(self):
        return '%s' % self.name
    name = models.CharField(u'название', max_length=100)
    car_type = models.CharField(u'модель автомобиля', max_length=15, choices=CAR_TYPE)
    price = models.DecimalField(u'цена', max_digits=12, decimal_places=2)


class TechLiquids(models.Model):
    class Meta:
        verbose_name_plural = u'технические жидкости'
        verbose_name = u'тех.жидкость'

    def __unicode__(self):
        return '%s' % self.name
    name = models.CharField(u'название', max_length=100)
    car_type = models.CharField(u'модель автомобиля', max_length=15, choices=CAR_TYPE)
    amount = models.DecimalField(u'кол-во, шт', max_digits=9, decimal_places=2, default=1.00)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)


class Service(models.Model):
    class Meta:
        verbose_name_plural = u'услуги'
        verbose_name = u'услуга'

    def __unicode__(self):
        return '%s' % self.name
    type = models.CharField(u'тип', max_length=20, choices=SERVICE_TYPE)
    name = models.CharField(u'название', max_length=100)
    car = models.CharField(u'модель автомобиля', max_length=15, choices=CAR_TYPE)
    price = models.DecimalField(u'цена', max_digits=12, decimal_places=2)
    price_cons = models.DecimalField(u'стоимость расходных материалов', max_digits=12, decimal_places=2, blank=True, null=True)
    spares = models.ManyToManyField(Spares, verbose_name=u'запчасти', blank=True, null=True)
    techliq = models.ManyToManyField(TechLiquids, verbose_name=u'тех.жидкости', blank=True, null=True)

