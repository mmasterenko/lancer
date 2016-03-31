# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0029_auto_20160314_1100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actions',
            options={'ordering': ('id',), 'verbose_name': '\u0430\u043a\u0446\u0438\u044e', 'verbose_name_plural': '\u0430\u043a\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='diagnostic',
            options={'ordering': ('id',), 'verbose_name': '\u0422\u041e', 'verbose_name_plural': '\u0422\u041e'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('id',), 'verbose_name': '\u043d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u043d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('id',), 'verbose_name': '\u0443\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterField(
            model_name='spares',
            name='number',
            field=models.CharField(null=True, default=None, max_length=25, blank=True, unique=True, verbose_name='\u043d\u043e\u043c\u0435\u0440'),
        ),
    ]
