# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0040_auto_20160321_2227'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='spares',
            name='car',
        ),
    ]
