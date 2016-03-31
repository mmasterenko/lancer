# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0036_auto_20160321_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='meta_desc',
            field=models.CharField(help_text=b'<meta name="description">', max_length=100, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='meta_keywords',
            field=models.CharField(help_text=b'<meta name="keywords">', max_length=100, null=True, verbose_name=b'Keywords', blank=True),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='title',
            field=models.CharField(help_text=b'<title>', max_length=100, null=True, verbose_name=b'Title', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='meta_desc',
            field=models.CharField(help_text=b'<meta name="description">', max_length=100, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='meta_keywords',
            field=models.CharField(help_text=b'<meta name="keywords">', max_length=100, null=True, verbose_name=b'Keywords', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(help_text=b'<title>', max_length=100, null=True, verbose_name=b'Title', blank=True),
        ),
    ]
