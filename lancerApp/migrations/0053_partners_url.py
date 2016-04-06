# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0052_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='url',
            field=models.URLField(default=b'', verbose_name='URL', blank=True),
        ),
    ]
