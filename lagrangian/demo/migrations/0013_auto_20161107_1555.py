# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0012_auto_20161107_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpost',
            name='Birthday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
