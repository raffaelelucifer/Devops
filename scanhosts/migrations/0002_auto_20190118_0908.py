# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='mac',
            field=models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u7269\u7406\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='sn',
            field=models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u5e8f\u5217\u53f7'),
        ),
    ]
