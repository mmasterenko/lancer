# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0044_auto_20160322_1512'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([('name', 'price')]),
        ),
    ]
