# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0030_auto_20160317_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spares',
            name='number',
            field=models.CharField(default=None, max_length=25, null=True, verbose_name='\u043d\u043e\u043c\u0435\u0440', blank=True),
        ),
    ]
