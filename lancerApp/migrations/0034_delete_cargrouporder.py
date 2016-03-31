# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0033_auto_20160318_2353'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarGroupOrder',
        ),
    ]
