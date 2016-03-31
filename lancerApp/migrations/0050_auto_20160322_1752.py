# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0049_service_car_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='car_name',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
        ),
    ]
