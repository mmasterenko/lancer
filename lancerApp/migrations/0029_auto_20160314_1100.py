# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0028_auto_20160314_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnostic',
            options={'verbose_name': '\u0422\u041e', 'verbose_name_plural': '\u0422\u041e'},
        ),
        migrations.RemoveField(
            model_name='diagnostic',
            name='cars',
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u043c\u0430\u0448\u0438\u043d\u044b', to='lancerApp.Car', null=True),
        ),
    ]
