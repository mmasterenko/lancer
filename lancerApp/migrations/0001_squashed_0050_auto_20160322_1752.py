# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lancerApp.model_mixins
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [(b'lancerApp', '0001_initial'), (b'lancerApp', '0002_auto_20160116_0148'), (b'lancerApp', '0003_auto_20160116_1331'), (b'lancerApp', '0004_auto_20160116_1810'), (b'lancerApp', '0005_spares'), (b'lancerApp', '0006_auto_20160116_2001'), (b'lancerApp', '0007_auto_20160116_2207'), (b'lancerApp', '0008_auto_20160116_2230'), (b'lancerApp', '0009_auto_20160116_2243'), (b'lancerApp', '0010_auto_20160116_2247'), (b'lancerApp', '0011_auto_20160117_1538'), (b'lancerApp', '0012_auto_20160117_1615'), (b'lancerApp', '0013_actions_generalinfo_news_stuff'), (b'lancerApp', '0014_generalinfo_feedbackurl'), (b'lancerApp', '0015_auto_20160128_1939'), (b'lancerApp', '0016_auto_20160128_2226'), (b'lancerApp', '0017_auto_20160205_1756'), (b'lancerApp', '0018_spares_service_type'), (b'lancerApp', '0019_auto_20160228_1909'), (b'lancerApp', '0020_spares_number'), (b'lancerApp', '0021_auto_20160228_2259'), (b'lancerApp', '0022_auto_20160229_1326'), (b'lancerApp', '0023_cargrouporder'), (b'lancerApp', '0024_auto_20160229_1410'), (b'lancerApp', '0025_auto_20160301_1533'), (b'lancerApp', '0026_auto_20160301_1538'), (b'lancerApp', '0027_auto_20160302_1439'), (b'lancerApp', '0028_auto_20160314_1014'), (b'lancerApp', '0029_auto_20160314_1100'), (b'lancerApp', '0030_auto_20160317_1343'), (b'lancerApp', '0031_auto_20160317_1344'), (b'lancerApp', '0032_auto_20160318_0033'), (b'lancerApp', '0033_auto_20160318_2353'), (b'lancerApp', '0034_delete_cargrouporder'), (b'lancerApp', '0035_auto_20160321_1819'), (b'lancerApp', '0036_auto_20160321_1847'), (b'lancerApp', '0037_auto_20160321_1855'), (b'lancerApp', '0038_auto_20160321_1857'), (b'lancerApp', '0039_auto_20160321_1935'), (b'lancerApp', '0040_auto_20160321_2227'), (b'lancerApp', '0041_auto_20160322_1448'), (b'lancerApp', '0042_auto_20160322_1458'), (b'lancerApp', '0043_auto_20160322_1506'), (b'lancerApp', '0044_auto_20160322_1512'), (b'lancerApp', '0045_auto_20160322_1538'), (b'lancerApp', '0046_auto_20160322_1611'), (b'lancerApp', '0047_auto_20160322_1617'), (b'lancerApp', '0048_auto_20160322_1655'), (b'lancerApp', '0049_service_car_name'), (b'lancerApp', '0050_auto_20160322_1752')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engine', models.CharField(max_length=4, verbose_name='\u041e\u0431\u044a\u0435\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f', choices=[(b'1.4', '1.4'), (b'1.6', '1.6'), (b'1.8', '1.8'), (b'2.0', '2.0')])),
                ('transmission', models.CharField(max_length=4, verbose_name='\u041a\u043e\u0440\u043e\u0431\u043a\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447', choices=[(b'auto', '\u0410\u0432\u0442\u043e\u043c\u0430\u0442'), (b'mech', '\u041c\u0435\u0445\u0430\u043d\u0438\u043a\u0430')])),
                ('type', models.CharField(max_length=20, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX')])),
            ],
            options={
                'verbose_name_plural': '\u041c\u0430\u0448\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, verbose_name='\u0422\u0438\u043f', choices=[(b'oil', b'\xd0\x97\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb6\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9'), (b'wheel', b'\xd0\xa0\xd1\x83\xd0\xbb\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'), (b'brake', b'\xd0\xa2\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0'), (b'chassis', b'\xd0\xa5\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c'), (b'engine', b'\xd0\x94\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'), (b'transmiss', b'\xd0\xa2\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbc\xd0\xb8\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'), (b'electro', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0')])),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('car', models.CharField(max_length=15, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX')])),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=12, decimal_places=2)),
                ('price_cons', models.DecimalField(null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432', max_digits=12, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0430',
            },
        ),
        migrations.CreateModel(
            name='Spares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('car_type', models.CharField(max_length=15, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX')])),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=12, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': '\u0417\u0430\u043f\u0447\u0430\u0441\u0442\u0438',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='spares',
            field=models.ManyToManyField(to=b'lancerApp.Spares', null=True, verbose_name='\u0417\u0430\u043f\u0447\u0430\u0441\u0442\u0438', blank=True),
        ),
        migrations.CreateModel(
            name='TechLiquids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('price', models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=9, decimal_places=2)),
            ],
            options={
                'verbose_name': '\u0442\u0435\u0445.\u0436\u0438\u0434\u043a\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': '\u043c\u0430\u0448\u0438\u043d\u0430', 'verbose_name_plural': '\u043c\u0430\u0448\u0438\u043d\u044b'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '\u0443\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='spares',
            options={'verbose_name': '\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u044c', 'verbose_name_plural': '\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0438'},
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together=set([('type', 'engine', 'transmission')]),
        ),
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([('name', 'car_type')]),
        ),
        migrations.AddField(
            model_name='service',
            name='techliq',
            field=models.ManyToManyField(to=b'lancerApp.TechLiquids', verbose_name='\u0442\u0435\u0445.\u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='car',
            field=models.CharField(max_length=15, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0442\u0438\u043f', choices=[(b'oil', b'\xd0\x97\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb6\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9'), (b'wheel', b'\xd0\xa0\xd1\x83\xd0\xbb\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'), (b'brake', b'\xd0\xa2\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0'), (b'chassis', b'\xd0\xa5\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c'), (b'engine', b'\xd0\x94\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'), (b'transmiss', b'\xd0\xa2\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbc\xd0\xb8\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'), (b'electro', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0')]),
        ),
        migrations.AddField(
            model_name='spares',
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
            field=models.ManyToManyField(to=b'lancerApp.Spares', verbose_name='\u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0438', blank=True),
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
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([('name', 'car')]),
        ),
        migrations.RemoveField(
            model_name='spares',
            name='car_type',
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(default=b'all', max_length=4, verbose_name='\u043e\u0431\u044a\u0435\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f', choices=[(b'1.4', '1.4'), (b'1.6', '1.6'), (b'1.8', '1.8'), (b'2.0', '2.0'), (b'all', '\u043b\u044e\u0431\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'all', max_length=4, verbose_name='\u043a\u043e\u0440\u043e\u0431\u043a\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447', choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430'), (b'all', '\u043b\u044e\u0431\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer 10'), (b'evo', b'Evolution 6-10'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_cons',
            field=models.DecimalField(null=True, verbose_name='\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432', max_digits=9, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0438\u043f', choices=[(b'oil', b'\xd0\x97\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb6\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9'), (b'wheel', b'\xd0\xa0\xd1\x83\xd0\xbb\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'), (b'brake', b'\xd0\xa2\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0'), (b'chassis', b'\xd0\xa5\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c'), (b'engine', b'\xd0\x94\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'), (b'transmiss', b'\xd0\xa2\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbc\xd0\xb8\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'), (b'electro', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0'), (b'other', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb5')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='price',
            field=models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=9, decimal_places=2),
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=80, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('img', models.ImageField(upload_to=b'images/original', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name_plural': '\u0410\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_phone', models.CharField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432 "\u0448\u0430\u043f\u043a\u0435"', max_length=20, verbose_name='\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', max_length=254, verbose_name='e-mail')),
                ('address', models.CharField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432 "\u0448\u0430\u043f\u043a\u0435"', max_length=60, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('workhours', models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u0447\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('phones', models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b')),
                ('about', models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435', verbose_name='\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438')),
                ('footerText', models.TextField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432\u043d\u0438\u0437\u0443', verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0432 \u0444\u0443\u0442\u0435\u0440\u0435')),
                ('feedbackURL', models.URLField(default=b'http://www.forum.lancer-club.ru/index.php?showtopic=117021', help_text='\u0441\u0441\u044b\u043b\u043a\u0430 \u0432 \u043c\u0435\u043d\u044e "\u041e\u0422\u0417\u042b\u0412\u042b"', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u043e\u0440\u0443\u043c')),
                ('is_smsing', models.BooleanField(default=True, help_text='\u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u044d\u0442\u0443 \u043e\u043f\u0446\u0438\u044e, \u0435\u0441\u043b\u0438 \u0445\u043e\u0442\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0441 \u0432\u0430\u0448\u0435\u0433\u043e \u0421\u041c\u0421-\u0441\u0447\u0435\u0442\u0430 \u041d\u0415 \u0441\u043f\u0438\u0441\u044b\u0432\u0430\u043b\u0438\u0441\u044c \u0434\u0435\u043d\u044c\u0433\u0438', verbose_name='\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443 \u0421\u041c\u0421')),
                ('sms_phone', models.CharField(default=b'', help_text='\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435: 79213332211', max_length=20, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d \u0434\u043b\u044f \u0421\u041c\u0421')),
                ('meta_desc', models.CharField(help_text=b'&lt;meta name="description"&gt;', max_length=100, null=True, verbose_name=b'Description', blank=True)),
                ('meta_keywords', models.CharField(help_text=b'&lt;meta name="keywords"&gt;', max_length=100, null=True, verbose_name=b'Keywords', blank=True)),
                ('title', models.CharField(help_text=b'&lt;title&gt;', max_length=100, null=True, verbose_name=b'Title', blank=True)),
                ('apikey', models.CharField(default=b'', help_text='api-key \u0434\u043b\u044f smspilot.ru. \u041d\u0415 \u043c\u0435\u043d\u044f\u0442\u044c !', max_length=100, verbose_name='api-key')),
                ('recipient', models.EmailField(default=b'MitsubishiLancerService@gmail.com', help_text='\u043d\u0430 \u044d\u0442\u043e\u0442 email \u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u0430, \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0441 \u0441\u0430\u0439\u0442\u0430', max_length=254, verbose_name='e-mail', blank=True)),
                ('sender', models.CharField(default=b'no-reply@mitsubishi4wd.ru', help_text='\u0431\u0443\u0434\u0435\u0442 \u0443\u043a\u0430\u0437\u0430\u043d\u043e \u0432 \u043f\u043e\u043b\u0435 \u041e\u0442:', max_length=100, verbose_name='\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c', blank=True)),
                ('subject', models.CharField(default='\u043f\u0438\u0441\u044c\u043c\u043e \u0441 \u0441\u0430\u0439\u0442\u0430 \u043b\u0430\u043d\u0441\u0435\u0440-\u0441\u0435\u0440\u0432\u0438\u0441.\u0440\u0444', max_length=100, verbose_name='\u0442\u0435\u043c\u0430 \u043f\u0438\u0441\u044c\u043c\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u043e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u043e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=80, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('url', lancerApp.model_mixins.SlugNullField(null=True, default=None, max_length=90, blank=True, help_text='URI \u043f\u043e\u0434 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u044c. \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: /udivitelnaya-novost/', unique=True, verbose_name='URI')),
                ('meta_desc', models.CharField(max_length=100, null=True, verbose_name=b'meta description', blank=True)),
                ('meta_keywords', models.CharField(max_length=100, null=True, verbose_name=b'meta keywords', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'<title>', blank=True)),
            ],
            options={
                'verbose_name': '\u043d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u043d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f')),
                ('surname', models.CharField(max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('position', models.CharField(max_length=50, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('desc', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('photo', models.ImageField(upload_to=b'images/original', verbose_name='\u0424\u043e\u0442\u043e')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430',
                'verbose_name_plural': '\u043d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430',
            },
        ),
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
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('type', 'name', 'car')]),
        ),
        migrations.AddField(
            model_name='spares',
            name='service_type',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='\u0442\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', choices=[(b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AddField(
            model_name='spares',
            name='number',
            field=models.CharField(default=None, max_length=25, null=True, verbose_name='\u043d\u043e\u043c\u0435\u0440', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=20, null=True, verbose_name='\u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0438\u043f', choices=[(b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AddField(
            model_name='car',
            name='subtype',
            field=models.CharField(max_length=20, null=True, verbose_name='\u043f\u043e\u0434\u0432\u0438\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'all', max_length=4, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f', choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'all', '\u043b\u044e\u0431\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0438\u0434', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'all', '\u0412\u0441\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', to='lancerApp.Car', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together=set([('type', 'subtype', 'engine', 'transmission')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f', blank=True, to='lancerApp.Car', null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='subtype',
            field=models.CharField(max_length=20, null=True, verbose_name='\u043f\u043e\u0434\u0432\u0438\u0434 \u0430/\u043c', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f', choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0438\u0434 \u0430/\u043c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', choices=[(b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=20, verbose_name='\u0432\u0438\u0434 \u0430/\u043c', choices=[(b'lancer9', b'Lancer 9'), (b'lancer10', b'Lancer X'), (b'evo', b'Evolution'), (b'asx', b'Lancer ASX'), (b'out_classic', b'OutLander Classic'), (b'out_xl', b'OutLander XL'), (b'out3', b'OutLander III'), (b'pajero', b'Pajero III-IV'), (b'paj_sport', b'Pajero Sport'), (b'l200', b'L-200')]),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='cars',
            field=models.ManyToManyField(to=b'lancerApp.Car', verbose_name='\u043c\u043e\u0434\u0435\u043b\u0438 \u043c\u0430\u0448\u0438\u043d'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='services',
            field=models.ManyToManyField(to=b'lancerApp.Service', verbose_name='\u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterModelOptions(
            name='diagnostic',
            options={'verbose_name': '\u0422\u041e', 'verbose_name_plural': '\u0422\u041e'},
        ),
        migrations.RemoveField(
            model_name='diagnostic',
            name='cars',
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='car',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u043c\u0430\u0448\u0438\u043d\u044b', to='lancerApp.Car', null=True),
        ),
        migrations.AlterModelOptions(
            name='actions',
            options={'ordering': ('id',), 'verbose_name': '\u0430\u043a\u0446\u0438\u044e', 'verbose_name_plural': '\u0430\u043a\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='diagnostic',
            options={'ordering': ('id',), 'verbose_name': '\u0422\u041e', 'verbose_name_plural': '\u0422\u041e'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('id',), 'verbose_name': '\u043d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u043d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('id',), 'verbose_name': '\u0443\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('type', 'name', 'car', 'price')]),
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
        migrations.AlterField(
            model_name='news',
            name='url',
            field=lancerApp.model_mixins.SlugNullField(null=True, default=None, max_length=90, blank=True, help_text='URL \u043f\u043e\u0434 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u044c. \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: /udivitelnaya-novost/', unique=True, verbose_name='URL'),
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
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='spares',
            name='car',
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'', choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f')], max_length=4, blank=True, null=True, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'', max_length=4, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f', blank=True, choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=b'', max_length=4, verbose_name='\u0442\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f', blank=True, choices=[(b'auto', '\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'mech', '\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f'), (b'', '')]),
        ),
        migrations.AlterUniqueTogether(
            name='spares',
            unique_together=set([('name', 'price')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='number',
            field=models.CharField(default=b'', max_length=25, verbose_name='\u043d\u043e\u043c\u0435\u0440', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', choices=[(b'', ''), (b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='service_type',
            field=models.CharField(default=b'', max_length=15, verbose_name='\u0442\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', blank=True, choices=[(b'', ''), (b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', choices=[(b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AlterField(
            model_name='spares',
            name='service_type',
            field=models.CharField(default=b'', max_length=15, verbose_name='\u0442\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', blank=True, choices=[(b'to', '\u0422\u0435\u0445.\u043e\u0441\u043c\u043e\u0442\u0440'), (b'oil', '\u0417\u0430\u043c\u0435\u043d\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439'), (b'wheel', '\u0420\u0443\u043b\u0435\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435'), (b'brake', '\u0422\u043e\u0440\u043c\u043e\u0437\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), (b'chassis', '\u0425\u043e\u0434\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u044c'), (b'engine', '\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c'), (b'transmiss', '\u0422\u0440\u0430\u043d\u0441\u043c\u0438\u0441\u0441\u0438\u044f'), (b'electro', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u043a\u0430'), (b'other', '\u0414\u0440\u0443\u0433\u043e\u0435')]),
        ),
        migrations.AddField(
            model_name='service',
            name='car_name',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
        ),
    ]
