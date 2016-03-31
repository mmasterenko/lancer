# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0045_auto_20160322_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spares',
            name='number',
            field=models.CharField(default=b'', max_length=25, verbose_name='\u043d\u043e\u043c\u0435\u0440', blank=True),
        ),
    ]
