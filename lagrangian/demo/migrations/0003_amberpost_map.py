# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_amberpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='amberpost',
            name='Map',
            field=location_field.models.plain.PlainLocationField(default=datetime.datetime(2016, 11, 3, 20, 34, 25, 744154, tzinfo=utc), max_length=63),
            preserve_default=False,
        ),
    ]
