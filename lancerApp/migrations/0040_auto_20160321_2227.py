# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0039_auto_20160321_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='recipient',
            field=models.EmailField(default=b'MitsubishiLancerService@gmail.com', help_text='\u043d\u0430 \u044d\u0442\u043e\u0442 email \u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u0430, \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0441 \u0441\u0430\u0439\u0442\u0430', max_length=254, verbose_name='e-mail', blank=True),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='sender',
            field=models.CharField(default=b'no-reply@mitsubishi4wd.ru', help_text='\u0431\u0443\u0434\u0435\u0442 \u0443\u043a\u0430\u0437\u0430\u043d\u043e \u0432 \u043f\u043e\u043b\u0435 \u041e\u0442:', max_length=100, verbose_name='\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c', blank=True),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='subject',
            field=models.CharField(default='\u043f\u0438\u0441\u044c\u043c\u043e \u0441 \u0441\u0430\u0439\u0442\u0430 \u043b\u0430\u043d\u0441\u0435\u0440-\u0441\u0435\u0440\u0432\u0438\u0441.\u0440\u0444', max_length=100, verbose_name='\u0442\u0435\u043c\u0430 \u043f\u0438\u0441\u044c\u043c\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='about',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='email',
            field=models.EmailField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='phones',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='workhours',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u0447\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
    ]
