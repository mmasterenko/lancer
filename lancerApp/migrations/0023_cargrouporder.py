# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0022_auto_20160229_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarGroupOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, verbose_name='\u0432\u0438\u0434', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')])),
                ('order1', models.CharField(max_length=15, verbose_name=b'#1', choices=[(b'subtype', '\u043f\u043e\u0434\u0432\u0438\u0434'), (b'trans', '\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'engine', '\u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c')])),
                ('order2', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'#2', choices=[(b'subtype', '\u043f\u043e\u0434\u0432\u0438\u0434'), (b'trans', '\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'engine', '\u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c')])),
                ('order3', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'#3', choices=[(b'subtype', '\u043f\u043e\u0434\u0432\u0438\u0434'), (b'trans', '\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'engine', '\u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c')])),
            ],
            options={
                'verbose_name': '\u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0433\u0440\u0443\u043f\u043f\u0438\u0440\u043e\u0432\u043a\u0438 \u0430\u0432\u0442\u043e',
                'verbose_name_plural': '\u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0433\u0440\u0443\u043f\u043f\u0438\u0440\u043e\u0432\u043a\u0438 \u0430\u0432\u0442\u043e',
            },
        ),
    ]
