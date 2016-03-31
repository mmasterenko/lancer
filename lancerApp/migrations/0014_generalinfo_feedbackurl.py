# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancerApp', '0013_actions_generalinfo_news_stuff'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='feedbackURL',
            field=models.URLField(default=b'http://www.forum.lancer-club.ru/index.php?showtopic=117021', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u043e\u0440\u0443\u043c'),
        ),
    ]
