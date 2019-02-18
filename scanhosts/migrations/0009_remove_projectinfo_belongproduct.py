# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0008_remove_projectinfo_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinfo',
            name='belongproduct',
        ),
    ]
