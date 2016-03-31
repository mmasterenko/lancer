# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientArea', '0005_auto_20160220_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='car',
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': '\u043a\u043b\u0438\u0435\u043d\u0442', 'verbose_name_plural': '\u043a\u043b\u0438\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='visit',
            name='customer',
            field=models.ForeignKey(verbose_name='\u043a\u043b\u0438\u0435\u043d\u0442', to='clientArea.CustomUser'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
