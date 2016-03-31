# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0034_delete_cargrouporder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalinfo',
            name='car_evolution',
        ),
        migrations.RemoveField(
            model_name='generalinfo',
            name='car_lancer10',
        ),
        migrations.RemoveField(
            model_name='generalinfo',
            name='car_lancer9',
        ),
        migrations.RemoveField(
            model_name='generalinfo',
            name='car_lancerASX',
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='is_smsing',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='sms_phone',
            field=models.CharField(default=b'', max_length=20, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d \u0434\u043b\u044f \u0421\u041c\u0421'),
        ),
    ]
