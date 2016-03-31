# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lancerApp', '0018_spares_service_type'),
        ('clientArea', '0003_auto_20160217_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_one2one',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_number', models.CharField(max_length=9, verbose_name='\u0433\u043e\u0441. \u043d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e (\u043b\u043e\u0433\u0438\u043d)')),
                ('surname', models.CharField(max_length=20, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='\u0438\u043c\u044f', blank=True)),
                ('patronymic', models.CharField(max_length=20, null=True, verbose_name='\u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('note', models.TextField(null=True, verbose_name='\u0434\u043e\u043f.\u0438\u043d\u0444\u043e', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('car', models.ForeignKey(verbose_name='\u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c', blank=True, to='lancerApp.Car', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='car_number',
            field=models.CharField(max_length=9, verbose_name='\u0433\u043e\u0441. \u043d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e (\u043b\u043e\u0433\u0438\u043d)'),
        ),
    ]
