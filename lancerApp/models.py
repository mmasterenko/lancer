# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from .model_mixins import SlugNullField, SEOFieldsMixin

upload_path = 'images/original'

SERVICE_TYPE = (
    ('oil',       u'Замена жидкостей'),
    ('wheel',     u'Рулевое управление'),
    ('brake',     u'Тормозная система'),
    ('chassis',   u'Ходовая часть'),
    ('engine',    u'Двигатель'),
    ('transmiss', u'Трансмиссия'),
    ('electro',   u'Электрика'),
    ('other',   u'Другое'),
)


class GeneralInfo(models.Model):
    class Meta:
        verbose_name = u'общая информация'
        verbose_name_plural = u'общая информация'

    def __unicode__(self):
        return u'общая информация'

    main_phone = models.CharField(u'основной телефон', max_length=20)
    email = models.EmailField(u'e-mail')
    address = models.CharField(u'адрес', max_length=60)
    workhours = models.TextField(u'часы работы')
    phones = models.TextField(u'телефоны')
    about = models.TextField(u'о компании')
    footerText = models.TextField(u'текст в футере')
    feedbackURL = models.URLField(u'Ссылка на форум', default='http://www.forum.lancer-club.ru/index.php?showtopic=117021')

    car_lancer9 = models.TextField(u'Lancer 9')
    car_lancer10 = models.TextField(u'Lancer 10')
    car_evolution = models.TextField(u'Evolution')
    car_lancerASX = models.TextField(u'Mitsubishi ASX')


class News(SEOFieldsMixin, models.Model):
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'

    def __unicode__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('news', args=[self.id])

    header = models.CharField(u'Заголовок', max_length=80)
    text = models.TextField(u'Текст')
    date = models.DateField(u'Дата', default=now)
    uri_help_text = u'URI под которым будет доступна новость. например: /udivitelnaya-novost/'
    url = SlugNullField(u'URI', help_text=uri_help_text, null=True, blank=True, unique=True, max_length=90, default=None)


class Actions(models.Model):
    class Meta:
        verbose_name_plural = u'Акции'

    def __unicode__(self):
        return '%s' % self.header

    header = models.CharField(u'Заголовок', max_length=80)
    text = models.TextField(u'Текст', blank=True, null=True)
    img = models.ImageField(u'Картинка', upload_to=upload_path)


class Stuff(models.Model):
    class Meta:
        verbose_name = u'наша команда'
        verbose_name_plural = verbose_name

    @property
    def full_name(self):
        return '%s %s' % (self.name, self.surname)

    def __unicode__(self):
        return self.full_name

    name = models.CharField(u'Имя', max_length=50)
    surname = models.CharField(u'Фамилия', max_length=50)
    position = models.CharField(u'Должность', max_length=50)
    desc = models.TextField(u'Описание')
    photo = models.ImageField(u'Фото', upload_to=upload_path)


class Car(models.Model):
    class Meta:
        verbose_name_plural = u'машины'
        verbose_name = u'машина'
        unique_together = ('type', 'engine', 'transmission')

    CAR_TYPE = (
        ('lancer9', 'Lancer 9'),
        ('lancer10', 'Lancer 10'),
        ('evo', 'Evolution 6-10'),
        ('asx', 'Lancer ASX'),
        ('all', u'Все модели'),
    )

    TRANSMISSION_TYPE = (
        ('auto', u'автомат'),
        ('mech', u'механика'),
        ('all',  u'любая'),
    )

    ENGINE_CAPACITY = (
        ('1.4', u'1.4'),
        ('1.6', u'1.6'),
        ('1.8', u'1.8'),
        ('2.0', u'2.0'),
        ('all', u'любой'),
    )

    def __unicode__(self):
        result = '%s %s %s' % (self.get_type_display(), self.get_transmission_display(), self.get_engine_display())
        if self.transmission == 'all':
            result = '%s %s' % (self.get_type_display(), self.get_engine_display())
        if self.engine == 'all':
            result = '%s %s' % (self.get_type_display(), self.get_transmission_display())
        if self.transmission == self.engine == 'all':
            result = self.get_type_display()
        return result

    @property
    def name(self):
        return self.__unicode__()

    type = models.CharField(u'модель', max_length=20, choices=CAR_TYPE)
    engine = models.CharField(u'объем двигателя', max_length=4, choices=ENGINE_CAPACITY, default='all')
    transmission = models.CharField(u'коробка передач', max_length=4, choices=TRANSMISSION_TYPE, default='all')


class Spares(models.Model):
    class Meta:
        verbose_name_plural = u'запчасти'
        verbose_name = u'запчасть'
        unique_together = ('name', 'car')

    def __unicode__(self):
        return '%s' % self.name
    name = models.CharField(u'название', max_length=100)
    car = models.ForeignKey(Car, verbose_name=u'модель автомобиля', null=True, blank=True)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)


class TechLiquids(models.Model):
    class Meta:
        verbose_name_plural = u'технические жидкости'
        verbose_name = u'тех.жидкость'

    def __unicode__(self):
        return '%s' % self.name
    name = models.CharField(u'название', max_length=100)
    car = models.ForeignKey(Car, verbose_name=u'модель автомобиля', null=True, blank=True)
    amount = models.DecimalField(u'кол-во, шт', max_digits=9, decimal_places=2, default=1.00)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)


class Service(models.Model):
    class Meta:
        verbose_name_plural = u'услуги'
        verbose_name = u'услуга'
        unique_together = ('type', 'name', 'car')

    def __unicode__(self):
        return '%s' % self.name

    @property
    def type_name(self):
        for typ, name in SERVICE_TYPE:
            if self.type == typ:
                return name

    type = models.CharField(u'тип', max_length=15, choices=SERVICE_TYPE)
    name = models.CharField(u'название', max_length=100)
    car = models.ForeignKey(Car, verbose_name=u'модель автомобиля', null=True)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)
    price_cons = models.DecimalField(u'стоимость расходных материалов', max_digits=9, decimal_places=2, blank=True, null=True)
    spares = models.ManyToManyField(Spares, verbose_name=u'запчасти', blank=True)
    techliq = models.ManyToManyField(TechLiquids, verbose_name=u'тех.жидкости', blank=True)

