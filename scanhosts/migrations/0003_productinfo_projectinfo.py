# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0002_auto_20190118_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('leader', models.CharField(max_length=50, verbose_name='\u6280\u672f\u7ecf\u7406')),
                ('phonenumber', models.CharField(max_length=20, null=True, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('describtion', models.TextField(verbose_name='\u4ea7\u54c1\u63cf\u8ff0')),
            ],
            options={
                'db_table': 'ProductInfo',
                'verbose_name': '\u4ea7\u54c1\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u4ea7\u54c1\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('leader', models.CharField(max_length=50, verbose_name='\u9879\u76ee\u7ecf\u7406')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('runserver', models.CharField(max_length=200, verbose_name='\u8fd0\u884c\u670d\u52a1\u5668')),
                ('describtion', models.TextField(verbose_name='\u9879\u76ee\u63cf\u8ff0')),
            ],
            options={
                'db_table': 'ProjectInfo',
                'verbose_name': '\u9879\u76ee\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u9879\u76ee\u4fe1\u606f\u8868',
            },
        ),
    ]
