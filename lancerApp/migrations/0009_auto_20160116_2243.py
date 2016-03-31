# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0008_auto_20160116_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='techliquids',
            name='amount',
            field=models.DecimalField(default=1.0, verbose_name='\u041a\u043e\u043b-\u0432\u043e, \u0448\u0442', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='techliquids',
            name='price',
            field=models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=9, decimal_places=2),
        ),
    ]
