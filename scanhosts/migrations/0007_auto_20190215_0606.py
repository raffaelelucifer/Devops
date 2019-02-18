# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0006_auto_20190129_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinfo',
            old_name='runserver',
            new_name='server',
        ),
    ]
