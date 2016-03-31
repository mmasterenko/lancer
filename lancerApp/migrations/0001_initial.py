# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engine', models.CharField(max_length=4, verbose_name='', choices=[(b'1.4', '1.4'), (b'1.6', '1.6'), (b'1.8', '1.8'), (b'2.0', '2.0')])),
                ('transmission', models.CharField(max_length=4, verbose_name='', choices=[(b'auto', '\u0410\u041a\u041f'), (b'mech', '\u041c\u041a\u041f')])),
            ],
            options={
                'verbose_name_plural': '\u041c\u0430\u0448\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c')),
                ('desc', models.CharField(max_length=100, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('img_width', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('img_height', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('img', models.ImageField(default=b'', height_field=b'img_height', width_field=b'img_width', upload_to=b'images/cars', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name_plural': '\u041c\u043e\u0434\u0435\u043b\u0438 \u043c\u0430\u0448\u0438\u043d',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.ForeignKey(to='lancerApp.CarType'),
        ),
    ]
