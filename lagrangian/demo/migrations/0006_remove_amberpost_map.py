# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_amberpost_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amberpost',
            name='Map',
        ),
    ]
