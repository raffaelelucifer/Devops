# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0009_remove_projectinfo_belongproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='belongproduct',
            field=models.CharField(default=0, max_length=50, verbose_name='\u6240\u5c5e\u4ea7\u54c1\u7ebf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='server',
            field=models.CharField(default=None, max_length=200, verbose_name='\u8fd0\u884c\u670d\u52a1\u5668'),
            preserve_default=False,
        ),
    ]
