# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20161107_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpost',
            name='Birthday',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
