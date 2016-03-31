# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0023_cargrouporder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargrouporder',
            name='type',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u0432\u0438\u0434', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')]),
        ),
    ]
