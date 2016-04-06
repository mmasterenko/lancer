# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0051_auto_20160331_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('text', models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('img', models.ImageField(upload_to=b'images/original', null=True, verbose_name='\u043b\u043e\u0433\u043e\u0442\u0438\u043f', blank=True)),
            ],
            options={
                'verbose_name': '\u043f\u0430\u0440\u0442\u043d\u0451\u0440',
                'verbose_name_plural': '\u043f\u0430\u0440\u0442\u043d\u0451\u0440\u044b',
            },
        ),
    ]
