# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0005_auto_20190129_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinfo',
            old_name='describtion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='projectinfo',
            old_name='describtion',
            new_name='description',
        ),
    ]
