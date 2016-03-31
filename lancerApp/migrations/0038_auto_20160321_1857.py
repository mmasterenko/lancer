# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lancerApp.model_mixins


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0037_auto_20160321_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='url',
            field=lancerApp.model_mixins.SlugNullField(null=True, default=None, max_length=90, blank=True, help_text='URL \u043f\u043e\u0434 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u044c. \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: /udivitelnaya-novost/', unique=True, verbose_name='URL'),
        ),
    ]
