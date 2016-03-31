# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0021_auto_20160228_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='subtype',
            field=models.CharField(max_length=20, null=True, verbose_name='\u043f\u043e\u0434\u0432\u0438\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'all', max_length=4, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f', choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'all', '\u043b\u044e\u0431\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0438\u0434', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')]),
        ),
    ]
