# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0018_spares_service_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_number', models.CharField(max_length=9, verbose_name='\u0433\u043e\u0441. \u043d\u043e\u043c\u0435\u0440 \u043c\u0430\u0448\u0438\u043d\u044b (\u043b\u043e\u0433\u0438\u043d)')),
                ('password', models.CharField(max_length=128, verbose_name='\u043f\u0430\u0440\u043e\u043b\u044c')),
                ('surname', models.CharField(max_length=20, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='\u0438\u043c\u044f', blank=True)),
                ('patronymic', models.CharField(max_length=20, null=True, verbose_name='\u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('note', models.TextField(null=True, verbose_name='\u0434\u043e\u043f.\u0438\u043d\u0444\u043e', blank=True)),
                ('car', models.ForeignKey(verbose_name='\u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c', to='lancerApp.Car')),
            ],
            options={
                'verbose_name': '\u043a\u043b\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u043a\u043b\u0438\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u0434\u0430\u0442\u0430')),
                ('km', models.PositiveIntegerField(verbose_name='\u043f\u0440\u043e\u0431\u0435\u0433')),
                ('note', models.TextField(verbose_name='\u0434\u043e\u043f.\u0438\u043d\u0444\u043e')),
                ('customer', models.ForeignKey(verbose_name='\u043a\u043b\u0438\u0435\u043d\u0442', to='clientArea.Customer')),
                ('services', models.ManyToManyField(to='lancerApp.Service', verbose_name='\u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f',
            },
        ),
    ]
