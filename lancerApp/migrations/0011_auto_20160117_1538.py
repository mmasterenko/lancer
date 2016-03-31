# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0010_auto_20160116_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techliquids',
            name='car_type',
        ),
        migrations.AddField(
            model_name='spares',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', to='lancerApp.Car', null=True),
        ),
        migrations.AddField(
            model_name='techliquids',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', to='lancerApp.Car', null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=4, verbose_name='\u043e\u0431\u044a\u0435\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f', choices=[(b'1.4', '1.4'), (b'1.6', '1.6'), (b'1.8', '1.8'), (b'2.0', '2.0'), (b'all', '\u043b\u044e\u0431\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=4, verbose_name='\u043a\u043e\u0440\u043e\u0431\u043a\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447', choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430'), (b'all', '\u043b\u044e\u0431\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', to='lancerApp.Car', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_cons',
            field=models.DecimalField(null=True, verbose_name='\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='spares',
            field=models.ManyToManyField(to='lancerApp.Spares', verbose_name='\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='techliq',
            field=models.ManyToManyField(to='lancerApp.TechLiquids', verbose_name='\u0442\u0435\u0445.\u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0442\u0438\u043f', choices=[(b'oil', b'\xd0\x97\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb6\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9'), (b'wheel', b'\xd0\xa0\xd1\x83\xd0\xbb\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'), (b'brake', b'\xd0\xa2\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0'), (b'chassis', b'\xd0\xa5\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c'), (b'engine', b'\xd0\x94\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'), (b'transmiss', b'\xd0\xa2\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbc\xd0\xb8\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'), (b'electro', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0'), (b'other', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb5')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='spares',
            name='price',
            field=models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='techliquids',
            name='amount',
            field=models.DecimalField(default=1.0, verbose_name='\u043a\u043e\u043b-\u0432\u043e, \u0448\u0442', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='techliquids',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='techliquids',
            name='price',
            field=models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=9, decimal_places=2),
        ),
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([('name', 'car')]),
        ),
        migrations.RemoveField(
            model_name='spares',
            name='car_type',
        ),
    ]
