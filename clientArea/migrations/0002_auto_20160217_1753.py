# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientArea', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ('-date', '-id'), 'verbose_name': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='car',
            field=models.ForeignKey(verbose_name='\u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c', blank=True, to='lancerApp.Car', null=True),
        ),
    ]
