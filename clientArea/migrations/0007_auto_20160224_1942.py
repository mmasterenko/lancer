# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0018_spares_service_type'),
        ('clientArea', '0006_auto_20160223_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='spares',
            field=models.ManyToManyField(to='lancerApp.Spares', verbose_name='\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='techliqs',
            field=models.ManyToManyField(to='lancerApp.TechLiquids', verbose_name='\u0442\u0435\u0445.\u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438', blank=True),
        ),
    ]
