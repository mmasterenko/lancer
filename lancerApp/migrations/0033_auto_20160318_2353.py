# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0032_auto_20160318_0033'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('type', 'name', 'car', 'price')]),
        ),
    ]
