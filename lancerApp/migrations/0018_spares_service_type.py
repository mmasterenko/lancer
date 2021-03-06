# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0017_auto_20160205_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='spares',
            name='service_type',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='\u0442\u0438\u043f \u0440\u0430\u0431\u043e\u0442', choices=[(b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
    ]
