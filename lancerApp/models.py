# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from .model_mixins import SlugNullField, SEOFieldsMixin

upload_path = 'images/original'

SERVICE_TYPE = (
    ('to',        u'Техническое обслуживание'),
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
    ('lancer9',     'Lancer 9'),
    ('lancer10',    'Lancer X'),
    ('evo',         'Evolution'),
    ('asx',         'ASX'),
    ('out_classic', 'OutLander Classic'),
    ('out_xl',      'OutLander XL'),
    ('out3',        'OutLander III'),
    ('pajero',      'Pajero III-IV'),
    ('paj_sport',   'Pajero Sport'),
    ('l200',        'L-200'),
)


class GeneralInfo(SEOFieldsMixin, models.Model):
    general_help_text = u'отображается на всех страницах в "шапке"'
    about_help_text = u'отображается на главной странице'

    main_phone = models.CharField(u'основной телефон', max_length=20, help_text=general_help_text)
    email = models.EmailField(u'e-mail', help_text=about_help_text)
    address = models.CharField(u'адрес', max_length=60, help_text=general_help_text)
    workhours = models.TextField(u'часы работы', help_text=about_help_text)
    phones = models.TextField(u'телефоны', help_text=about_help_text)
    about = models.TextField(u'о компании', help_text=about_help_text)
    footerText = models.TextField(u'текст в футере', help_text=u'отображается на всех страницах внизу')
    feedbackURL = models.URLField(u'Ссылка на форум', help_text=u'ссылка в меню "ОТЗЫВЫ"',
                                  default='http://www.forum.lancer-club.ru/index.php?showtopic=117021')
    sms_phone = models.CharField(u'телефон для СМС', max_length=20, default='', help_text=u'в формате: 79213332211')
    is_smsing = models.BooleanField(u'включить отправку СМС', default=True,
                                    help_text=u'отключите эту опцию, если хотите, '
                                              u'чтобы с вашего СМС-счета НЕ списывались деньги')
    apikey = models.CharField(u'api-key', max_length=100, default='', help_text=u'api-key для smspilot.ru. НЕ менять !')
    sender = models.CharField(u'отправитель', default='no-reply@mitsubishi4wd.ru', max_length=100, blank=True,
                              help_text=u'будет указано в поле От:')
    subject = models.CharField(u'тема письма', default=u'письмо с сайта лансер-сервис.рф', max_length=100, blank=True)
    recipient = models.EmailField(u'e-mail', default='MitsubishiLancerService@gmail.com', blank=True,
                                  help_text=u'на этот email будут приходить письма, отправленные с сайта')

    class Meta:
        verbose_name = u'общая информация'
        verbose_name_plural = u'общая информация'

    def __unicode__(self):
        return u'общая информация'


class News(SEOFieldsMixin, models.Model):
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ('-date', '-id')

    def __unicode__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('news', args=[self.id])

    header = models.CharField(u'Заголовок', max_length=80)
    text = models.TextField(u'Текст')
    date = models.DateField(u'Дата', default=now)
    url_help_text = u'URL под которым будет доступна новость. например: /udivitelnaya-novost/'
    url = SlugNullField(u'URL', help_text=url_help_text, null=True, blank=True, unique=True, max_length=90, default=None)


class Actions(models.Model):
    class Meta:
        verbose_name_plural = u'акции'
        verbose_name = u'акцию'
        ordering = ('id',)

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
    TRANSMISSION_TYPE = (
        ('auto', u'автоматическая'),
        ('mech', u'механическая'),
        ('', u''),
    )

    type = models.CharField(u'вид а/м', max_length=20, choices=CAR_TYPE)
    subtype = models.CharField(u'подвид а/м', max_length=20, null=True, blank=True)
    engine = models.CharField(u'двигатель', max_length=20, null=True, blank=True)
    transmission = models.CharField(u'трансмиссия', max_length=4, choices=TRANSMISSION_TYPE, blank=True, default='')

    class Meta:
        verbose_name_plural = u'машины'
        verbose_name = u'машина'
        unique_together = ('type', 'subtype', 'engine', 'transmission')

    def get_transmission_display(self):
        if not self.transmission:
            return ''
        if self.transmission == 'mech':
            return u'механика'
        if self.transmission == 'auto':
            return u'автомат'

    def __unicode__(self):
        return '%s %s %s %s' % (self.get_type_display(), self.subtype, self.engine, self.get_transmission_display())

    @property
    def name(self):
        return self.__unicode__()


class Spares(models.Model):
    class Meta:
        verbose_name_plural = u'запчасти'
        verbose_name = u'запчасть'
        unique_together = ('name', 'price')

    def __unicode__(self):
        return u'%s (%d р)' % (self.name, self.price)
    name = models.CharField(u'название', max_length=100)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)
    service_type = models.CharField(u'тип услуги', max_length=15, choices=SERVICE_TYPE, default='', blank=True)
    number = models.CharField(u'номер', max_length=25, blank=True, default='')


class TechLiquids(models.Model):
    class Meta:
        verbose_name_plural = u'технические жидкости'
        verbose_name = u'тех.жидкость'

    def __unicode__(self):
        return u'%s (%d р)' % (self.name, self.price)
    name = models.CharField(u'название', max_length=100)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)


class Service(models.Model):
    type = models.CharField(u'тип услуги', max_length=15, choices=SERVICE_TYPE)
    name = models.CharField(u'название', max_length=100)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2)
    price_cons = models.DecimalField(u'стоимость расходных материалов', max_digits=9, decimal_places=2, default=0)

    car = models.ForeignKey(Car, verbose_name=u'модель автомобиля', null=True, on_delete=models.SET_NULL)
    car_name = models.CharField(max_length=200, null=True, blank=True, default='')

    spares = models.ManyToManyField(Spares, verbose_name=u'запчасти', blank=True)
    techliq = models.ManyToManyField(TechLiquids, verbose_name=u'тех.жидкости', blank=True)

    class Meta:
        verbose_name_plural = u'услуги'
        verbose_name = u'услуга'
        unique_together = ('type', 'name', 'car', 'price')
        ordering = ('id',)

    def __unicode__(self):
        return u'%s на %s (%d р)' % (self.name, self.car_name, self.price)

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


# тех.осмотр
class Diagnostic(models.Model):
    name = models.CharField(u'название', max_length=50)
    car = models.ForeignKey(Car, verbose_name=u'модель машины', null=True)
    services = models.ManyToManyField(Service, verbose_name=u'работы')

    class Meta:
        verbose_name_plural = u'ТО'
        verbose_name = u'ТО'
        ordering = ('id',)

    def __unicode__(self):
        return u'%s на %s' % (self.name, self.car)
