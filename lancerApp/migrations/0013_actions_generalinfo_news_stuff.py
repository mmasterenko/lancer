# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lancerApp.model_mixins
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0012_auto_20160117_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=80, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('img', models.ImageField(upload_to=b'images/original', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('url', lancerApp.model_mixins.SlugNullField(null=True, default=None, max_length=90, blank=True, help_text='URI \u043f\u043e\u0434 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u0430\u043a\u0446\u0438\u044f. \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: /novaya-akciya/', unique=True, verbose_name='URI')),
            ],
            options={
                'verbose_name_plural': '\u0410\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_phone', models.CharField(max_length=20, verbose_name='\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('address', models.CharField(max_length=60, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('workhours', models.TextField(verbose_name='\u0447\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('phones', models.TextField(verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b')),
                ('about', models.TextField(verbose_name='\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438')),
                ('footerText', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0432 \u0444\u0443\u0442\u0435\u0440\u0435')),
                ('car_lancer9', models.TextField(verbose_name='Lancer 9')),
                ('car_lancer10', models.TextField(verbose_name='Lancer 10')),
                ('car_evolution', models.TextField(verbose_name='Evolution')),
                ('car_lancerASX', models.TextField(verbose_name='Lancer ASX')),
            ],
            options={
                'verbose_name': '\u043e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u043e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=80, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('url', lancerApp.model_mixins.SlugNullField(null=True, default=None, max_length=90, blank=True, help_text='URI \u043f\u043e\u0434 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u044c. \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: /udivitelnaya-novost/', unique=True, verbose_name='URI')),
            ],
            options={
                'verbose_name': '\u043d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u043d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f')),
                ('surname', models.CharField(max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('position', models.CharField(max_length=50, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('desc', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('photo', models.ImageField(upload_to=b'images/original', verbose_name='\u0424\u043e\u0442\u043e')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430',
                'verbose_name_plural': '\u043d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430',
            },
        ),
    ]
