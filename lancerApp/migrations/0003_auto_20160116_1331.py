# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0002_auto_20160116_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=4, verbose_name='\u041e\u0431\u044a\u0435\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f', choices=[(b'1.4', '1.4'), (b'1.6', '1.6'), (b'1.8', '1.8'), (b'2.0', '2.0')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=4, verbose_name='\u041a\u043e\u0440\u043e\u0431\u043a\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447', choices=[(b'auto', '\u0410\u041a\u041f'), (b'mech', '\u041c\u041a\u041f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX')]),
        ),
        migrations.DeleteModel(
            name='CarType',
        ),
    ]
