# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0038_auto_20160321_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='apikey',
            field=models.CharField(default=b'', help_text='api-key \u0434\u043b\u044f smspilot.ru. \u041d\u0415 \u043c\u0435\u043d\u044f\u0442\u044c !', max_length=100, verbose_name='api-key'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='meta_desc',
            field=models.CharField(help_text=b'&lt;meta name="description"&gt;', max_length=100, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='meta_keywords',
            field=models.CharField(help_text=b'&lt;meta name="keywords"&gt;', max_length=100, null=True, verbose_name=b'Keywords', blank=True),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='title',
            field=models.CharField(help_text=b'&lt;title&gt;', max_length=100, null=True, verbose_name=b'Title', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='meta_desc',
            field=models.CharField(help_text=b'&lt;meta name="description"&gt;', max_length=100, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='meta_keywords',
            field=models.CharField(help_text=b'&lt;meta name="keywords"&gt;', max_length=100, null=True, verbose_name=b'Keywords', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(help_text=b'&lt;title&gt;', max_length=100, null=True, verbose_name=b'Title', blank=True),
        ),
    ]
