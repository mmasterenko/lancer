# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0015_auto_20160128_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='meta_desc',
            field=models.CharField(max_length=100, null=True, verbose_name=b'meta description', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_keywords',
            field=models.CharField(max_length=100, null=True, verbose_name=b'meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name=b'<title>', blank=True),
        ),
    ]
