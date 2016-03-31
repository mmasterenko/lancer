# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0014_generalinfo_feedbackurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actions',
            name='date',
        ),
        migrations.RemoveField(
            model_name='actions',
            name='url',
        ),
        migrations.AlterField(
            model_name='actions',
            name='text',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='car_lancerASX',
            field=models.TextField(verbose_name='Mitsubishi ASX'),
        ),
    ]
