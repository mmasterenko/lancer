# -*- coding: utf-8 -*-

from django.db import models
from lancerApp.models import Car, Service
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, car_number, last_name=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not car_number:
            raise ValueError(u'Car number must be set')
        user = self.model(car_number=car_number, last_name=last_name, is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name = u'клиент'
        verbose_name_plural = u'клиенты'

    def __unicode__(self):
        return self.get_abbrev_name_car()

    @property
    def full_name(self):
        return u'%s %s %s' % (self.last_name.title(),
                              self.first_name.title() if self.first_name else u'',
                              self.patronymic_name.title() if self.patronymic_name else u'')

    def get_abbrev_name(self):
        return u'%s %s %s' % (self.last_name.title(),
                              self.first_name[0].upper() + '.' if self.first_name else u'',
                              self.patronymic_name[0].upper() + '.' if self.patronymic_name else u'')
    get_abbrev_name.short_description = u'ФИО'

    def get_abbrev_name_car(self):
        return u'%s %s' % (self.get_abbrev_name(), u'(%s)' % self.car if self.car else u'')
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

    USERNAME_FIELD = 'car_number'
    REQUIRED_FIELDS = ['last_name']

    is_staff = False

    car_number = models.CharField(u'гос. номер авто (логин)', max_length=9, unique=True)

    last_name = models.CharField(u'фамилия', max_length=20)
    first_name = models.CharField(u'имя', max_length=20, blank=True, null=True)
    patronymic_name = models.CharField(u'отчество', max_length=20, blank=True, null=True)

    note = models.TextField(u'доп.инфо', blank=True, null=True)
    car = models.ForeignKey(Car, verbose_name=u'автомобиль', blank=True, null=True)
    phone = models.CharField(u'телефон', max_length=20, blank=True, null=True)
    email = models.EmailField(u'e-mail', blank=True, null=True)
    is_active = models.BooleanField(u'активный', default=True,
                                    help_text=u'уберите эту галочку, если хотите деактивировать клиента')

    objects = CustomUserManager()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = u'%s %s' % (self.first_name if self.first_name else u'', self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name


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
    customer = models.ForeignKey(CustomUser, verbose_name=u'клиент')
    services = models.ManyToManyField(Service, verbose_name=u'оказанные услуги', blank=True)
    note = models.TextField(u'доп.инфо', blank=True, null=True)

