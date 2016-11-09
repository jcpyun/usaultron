# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20161103_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='policepost',
            name='Information',
            field=models.TextField(null=True, blank=True),
        ),
    ]
