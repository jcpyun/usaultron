# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_auto_20161107_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectpost',
            name='Birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='objectpost',
            name='Sex',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
        ),
    ]
