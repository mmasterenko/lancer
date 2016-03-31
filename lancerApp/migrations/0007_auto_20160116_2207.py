# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0006_auto_20160116_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='spares',
        ),
        migrations.AddField(
            model_name='service',
            name='spares',
            field=models.ManyToManyField(to='lancerApp.Spares', null=True, verbose_name='\u0417\u0430\u043f\u0447\u0430\u0441\u0442\u0438', blank=True),
        ),
    ]
