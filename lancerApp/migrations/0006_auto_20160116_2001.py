# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0005_spares'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='spares',
            field=models.ForeignKey(default=b'', verbose_name='\u0417\u0430\u043f\u0447\u0430\u0441\u0442\u044c', blank=True, to='lancerApp.Spares'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_cons',
            field=models.DecimalField(null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
