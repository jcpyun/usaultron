# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_remove_amberpost_map'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AmberPost',
            new_name='PolicePost',
        ),
    ]
