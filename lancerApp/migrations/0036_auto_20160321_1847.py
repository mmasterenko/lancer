# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0035_auto_20160321_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='about',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='address',
            field=models.CharField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432 "\u0448\u0430\u043f\u043a\u0435"', max_length=60, verbose_name='\u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='email',
            field=models.EmailField(help_text='\u043d\u0430 \u044d\u0442\u043e\u0442 email \u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u0430, \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0441 \u0441\u0430\u0439\u0442\u0430', max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='feedbackURL',
            field=models.URLField(default=b'http://www.forum.lancer-club.ru/index.php?showtopic=117021', help_text='\u0441\u0441\u044b\u043b\u043a\u0430 \u0432 \u043c\u0435\u043d\u044e "\u041e\u0422\u0417\u042b\u0412\u042b"', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u043e\u0440\u0443\u043c'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='footerText',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432\u043d\u0438\u0437\u0443', verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0432 \u0444\u0443\u0442\u0435\u0440\u0435'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='is_smsing',
            field=models.BooleanField(default=True, help_text='\u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u044d\u0442\u0443 \u043e\u043f\u0446\u0438\u044e, \u0435\u0441\u043b\u0438 \u0445\u043e\u0442\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0441 \u0432\u0430\u0448\u0435\u0433\u043e \u0421\u041c\u0421-\u0441\u0447\u0435\u0442\u0430 \u041d\u0415 \u0441\u043f\u0438\u0441\u044b\u0432\u0430\u043b\u0438\u0441\u044c \u0434\u0435\u043d\u044c\u0433\u0438', verbose_name='\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443 \u0421\u041c\u0421'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='main_phone',
            field=models.CharField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432 "\u0448\u0430\u043f\u043a\u0435"', max_length=20, verbose_name='\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='phones',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='sms_phone',
            field=models.CharField(default=b'', help_text='\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435: 79213332211', max_length=20, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d \u0434\u043b\u044f \u0421\u041c\u0421'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='workhours',
            field=models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u0447\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
    ]
