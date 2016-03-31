# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0043_auto_20160322_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'', max_length=4, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f', blank=True, choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'', '')]),
        ),
    ]
