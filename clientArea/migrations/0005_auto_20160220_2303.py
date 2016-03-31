# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0018_spares_service_type'),
        ('clientArea', '0004_auto_20160220_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('car_number', models.CharField(unique=True, max_length=9, verbose_name='\u0433\u043e\u0441. \u043d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e (\u043b\u043e\u0433\u0438\u043d)')),
                ('last_name', models.CharField(max_length=20, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('first_name', models.CharField(max_length=20, null=True, verbose_name='\u0438\u043c\u044f', blank=True)),
                ('patronymic_name', models.CharField(max_length=20, null=True, verbose_name='\u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('note', models.TextField(null=True, verbose_name='\u0434\u043e\u043f.\u0438\u043d\u0444\u043e', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='e-mail', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='\u0443\u0431\u0435\u0440\u0438\u0442\u0435 \u044d\u0442\u0443 \u0433\u0430\u043b\u043e\u0447\u043a\u0443, \u0435\u0441\u043b\u0438 \u0445\u043e\u0442\u0438\u0442\u0435 \u0434\u0435\u0430\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430', verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
                ('car', models.ForeignKey(verbose_name='\u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c', blank=True, to='lancerApp.Car', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='customer_one2one',
            name='car',
        ),
        migrations.RemoveField(
            model_name='customer_one2one',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer_one2one',
        ),
    ]
