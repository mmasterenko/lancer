# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0019_auto_20160228_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='spares',
            name='number',
            field=models.CharField(max_length=25, unique=True, null=True, verbose_name='\u043d\u043e\u043c\u0435\u0440', blank=True),
        ),
    ]
