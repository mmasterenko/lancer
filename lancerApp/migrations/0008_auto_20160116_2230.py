# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0007_auto_20160116_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechLiquids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('car_type', models.CharField(max_length=15, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX')])),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=12, decimal_places=2)),
            ],
            options={
                'verbose_name': '\u0442\u0435\u0445.\u0436\u0438\u0434\u043a\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': '\u043c\u0430\u0448\u0438\u043d\u0430', 'verbose_name_plural': '\u043c\u0430\u0448\u0438\u043d\u044b'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '\u0443\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='spares',
            options={'verbose_name': '\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u044c', 'verbose_name_plural': '\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0438'},
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together=set([('type', 'engine', 'transmission')]),
        ),
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([('name', 'car_type')]),
        ),
    ]
