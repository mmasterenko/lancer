# -*- coding: utf-8 -*-

from django.db import models


class CarType(models.Model):
    class Meta:
        verbose_name_plural = u'Модели машин'

    def __unicode__(self):
        return '%s' % self.name
    name = models.CharField(u'Модель', max_length=20)
    desc = models.CharField(u'Описание', max_length=100, blank=True)
    # img_width = models.PositiveSmallIntegerField(null=True, blank=True)
    # img_height = models.PositiveSmallIntegerField(null=True, blank=True)
    # img = models.ImageField(u'Картинка', upload_to='images/cars', default='', width_field='img_width', height_field='img_height')


class Car(models.Model):
    class Meta:
        verbose_name_plural = u'Машины'

    TRANSMISSION_CHOICES = (
        ('auto', u'АКП'),
        ('mech', u'МКП')
    )

    CAPACITY_CHOICES = (
        ('1.4', u'1.4'),
        ('1.6', u'1.6'),
        ('1.8', u'1.8'),
        ('2.0', u'2.0'),
    )

    def __unicode__(self):
        return '%s %s %s' % (self.type, self.engine, self.get_transmission_display())
    type = models.ForeignKey(CarType)
    engine = models.CharField(u'', max_length=4, choices=CAPACITY_CHOICES)
    transmission = models.CharField(u'', max_length=4, choices=TRANSMISSION_CHOICES)

