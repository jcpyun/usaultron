# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_remove_amberpost_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='amberpost',
            name='Map',
            field=location_field.models.plain.PlainLocationField(default=datetime.datetime(2016, 11, 3, 20, 38, 30, 95966, tzinfo=utc), max_length=63),
            preserve_default=False,
        ),
    ]
