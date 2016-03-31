# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0024_auto_20160229_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', to='lancerApp.Car', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together=set([('type', 'subtype', 'engine', 'transmission')]),
        ),
    ]
