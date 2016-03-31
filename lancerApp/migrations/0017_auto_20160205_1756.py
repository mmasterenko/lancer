# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0016_auto_20160128_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price_cons',
            field=models.DecimalField(default=0, verbose_name='\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0438\u043f', choices=[(b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', blank=True, to='lancerApp.Car', null=True),
        ),
        migrations.AlterField(
            model_name='techliquids',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', blank=True, to='lancerApp.Car', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('type', 'name', 'car')]),
        ),
    ]
