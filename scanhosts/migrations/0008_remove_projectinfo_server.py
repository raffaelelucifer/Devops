# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0007_auto_20190215_0606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinfo',
            name='server',
        ),
    ]
