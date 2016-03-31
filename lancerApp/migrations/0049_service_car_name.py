# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0048_auto_20160322_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='car_name',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
    ]
