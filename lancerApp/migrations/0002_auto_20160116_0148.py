# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartype',
            name='img',
        ),
        migrations.RemoveField(
            model_name='cartype',
            name='img_height',
        ),
        migrations.RemoveField(
            model_name='cartype',
            name='img_width',
        ),
        migrations.AlterField(
            model_name='cartype',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
