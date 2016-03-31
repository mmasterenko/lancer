# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientArea', '0002_auto_20160217_1753'),
    ]

    operations = [
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
            field=models.ManyToManyField(to='lancerApp.Service', verbose_name='\u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', blank=True),
        ),
    ]
