# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from .model_mixins import SlugNullField, SEOFieldsMixin

upload_path = 'images/original'

SERVICE_TYPE = (
    ('to',        u'Тех.осмотр'),
    ('oil',       u'Замена жидкостей'),
    ('wheel',     u'Рулевое управление'),
    ('brake',     u'Тормозная система'),
    ('chassis',   u'Ходовая часть'),
    ('engine',    u'Двигатель'),
    ('transmiss', u'Трансмиссия'),
    ('electro',   u'Электрика'),
    ('other',     u'Другое'),
)

CAR_TYPE = (
    ('lancer9', 'Lancer 9'),
    ('lancer10', 'Lancer X'),
    ('evo', 'Evolution'),
    ('asx', 'Lancer ASX'),
    ('all', u'Все модели'),
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


class CarGroupOrder(models.Model):
    GROUPS = (
        ('subtype', u'подвид'),
        ('trans',   u'трансмиссия'),
        ('engine',  u'двигатель'),
    )
    type = models.CharField(u'вид', max_length=20, choices=CAR_TYPE, unique=True)
    order1 = models.CharField('#1', max_length=15, choices=GROUPS)
    order2 = models.CharField('#2', max_length=15, choices=GROUPS, null=True, blank=True)
    order3 = models.CharField('#3', max_length=15, choices=GROUPS, null=True, blank=True)

    class Meta:
        verbose_name_plural = u'порядок группировки авто'
        verbose_name = u'порядок группировки авто'

    def __unicode__(self):
        return self.type


class Car(models.Model):
    TRANSMISSION_TYPE = (
        ('auto', u'автоматическая'),
        ('mech', u'механическая'),
        ('all',  u'любая'),
    )

    type = models.CharField(u'вид', max_length=20, choices=CAR_TYPE)
    subtype = models.CharField(u'подвид', max_length=20, null=True, blank=True)
    engine = models.CharField(u'двигатель', max_length=20, null=True, blank=True)
    transmission = models.CharField(u'трансмиссия', max_length=4, choices=TRANSMISSION_TYPE, default='all')

    class Meta:
        verbose_name_plural = u'машины'
        verbose_name = u'машина'
        unique_together = ('type', 'subtype', 'engine', 'transmission')

    def __unicode__(self):
        result = '%s %s %s' % (self.get_type_display(), self.get_transmission_display(), self.engine)
        if self.transmission == 'all':
            result = '%s %s' % (self.get_type_display(), self.engine)
        if self.engine == 'all' or not self.engine:
            result = '%s %s' % (self.get_type_display(), self.get_transmission_display())
        if self.transmission == 'all' and (self.engine == 'all' or not self.engine):
            result = self.get_type_display()
        return result

    @property
    def name(self):
        return self.__unicode__()


class Spares(models.Model):
    class Meta:
        verbose_name_plural = u'запчасти'
        verbose_name = u'запчасть'
        unique_together = ('name', 'car')

    def __unicode__(self):
        if self.car:
            return '%s (%s)' % (self.name, self.car.name)
        else:
            return '%s' % self.name
    name = models.CharField(u'название', max_length=100)
    car = models.ForeignKey(Car, verbose_name=u'модель автомобиля', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)
    service_type = models.CharField(u'тип работ', max_length=15, choices=SERVICE_TYPE, null=True, blank=True)
    number = models.CharField(u'номер', max_length=25, null=True, blank=True, unique=True)


class TechLiquids(models.Model):
    class Meta:
        verbose_name_plural = u'технические жидкости'
        verbose_name = u'тех.жидкость'

    def __unicode__(self):
        return '%s' % self.name
    name = models.CharField(u'название', max_length=100)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)


class Service(models.Model):
    type = models.CharField(u'тип', max_length=15, choices=SERVICE_TYPE)
    name = models.CharField(u'название', max_length=100)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)
    price_cons = models.DecimalField(u'стоимость расходных материалов', max_digits=9, decimal_places=2, default=0)

    car = models.ForeignKey(Car, verbose_name=u'модель автомобиля', null=True, on_delete=models.SET_NULL)

    spares = models.ManyToManyField(Spares, verbose_name=u'запчасти', blank=True)
    techliq = models.ManyToManyField(TechLiquids, verbose_name=u'тех.жидкости', blank=True)

    class Meta:
        verbose_name_plural = u'услуги'
        verbose_name = u'услуга'
        unique_together = ('type', 'name', 'car')

    def __unicode__(self):
        return u'%s на %s (%d руб)' % (self.name, self.car, self.price)

    @property
    def price_materials(self):
        spares_price_sum = sum([spare.price for spare in self.spares.all()])
        techliqs_price_sum = sum([tl.price for tl in self.techliq.all()])
        return sum([spares_price_sum, techliqs_price_sum, self.price_cons])

    @staticmethod
    def type2name(type):
        for typ, name in SERVICE_TYPE:
            if type == typ:
                return name

    @property
    def type_name(self):
        for typ, name in SERVICE_TYPE:
            if self.type == typ:
                return name

