# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0027_auto_20160302_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0438\u0434 \u0430/\u043c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'out_classic', b'OutLander Classic'), (b'out_xl', b'OutLander XL'), (b'out3', b'OutLander III'), (b'pajero', b'Pajero III-IV'), (b'paj_sport', b'Pajero Sport'), (b'l200', b'L-200')]),
        ),
        migrations.AlterField(
            model_name='cargrouporder',
            name='type',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u0432\u0438\u0434', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'out_classic', b'OutLander Classic'), (b'out_xl', b'OutLander XL'), (b'out3', b'OutLander III'), (b'pajero', b'Pajero III-IV'), (b'paj_sport', b'Pajero Sport'), (b'l200', b'L-200')]),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='cars',
            field=models.ManyToManyField(to='lancerApp.Car', verbose_name='\u043c\u043e\u0434\u0435\u043b\u0438 \u043c\u0430\u0448\u0438\u043d'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='services',
            field=models.ManyToManyField(to='lancerApp.Service', verbose_name='\u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
    ]
