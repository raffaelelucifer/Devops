# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0003_productinfo_projectinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='belongproduct',
            field=models.CharField(default=b'', max_length=50, verbose_name='\u6240\u5c5e\u4ea7\u54c1\u7ebf'),
        ),
    ]
