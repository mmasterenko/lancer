# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0018_spares_service_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techliquids',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='techliquids',
            name='car',
        ),
    ]
