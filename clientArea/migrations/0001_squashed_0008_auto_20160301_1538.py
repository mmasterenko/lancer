# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'clientArea', '0001_initial'), (b'clientArea', '0002_auto_20160217_1753'), (b'clientArea', '0003_auto_20160217_1947'), (b'clientArea', '0004_auto_20160220_1927'), (b'clientArea', '0005_auto_20160220_2303'), (b'clientArea', '0006_auto_20160223_1935'), (b'clientArea', '0007_auto_20160224_1942'), (b'clientArea', '0008_auto_20160301_1538')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lancerApp', '0001_squashed_0050_auto_20160322_1752'),
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
                ('services', models.ManyToManyField(to=b'lancerApp.Service', verbose_name='\u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ('-date', '-id'), 'verbose_name': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='car',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='km',
            field=models.PositiveIntegerField(null=True, verbose_name='\u043f\u0440\u043e\u0431\u0435\u0433', blank=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='note',
            field=models.TextField(null=True, verbose_name='\u0434\u043e\u043f.\u0438\u043d\u0444\u043e', blank=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='services',
            field=models.ManyToManyField(to=b'lancerApp.Service', verbose_name='\u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='car_number',
            field=models.CharField(max_length=9, verbose_name='\u0433\u043e\u0441. \u043d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e (\u043b\u043e\u0433\u0438\u043d)'),
        ),
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
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': '\u043a\u043b\u0438\u0435\u043d\u0442', 'verbose_name_plural': '\u043a\u043b\u0438\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='visit',
            name='customer',
            field=models.ForeignKey(verbose_name='\u043a\u043b\u0438\u0435\u043d\u0442', to='clientArea.CustomUser'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='visit',
            name='spares',
            field=models.ManyToManyField(to=b'lancerApp.Spares', verbose_name='\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='techliqs',
            field=models.ManyToManyField(to=b'lancerApp.TechLiquids', verbose_name='\u0442\u0435\u0445.\u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c', blank=True, to='lancerApp.Car', null=True),
        ),
    ]
