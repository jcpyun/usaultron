# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_objectpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpost',
            name='Age',
            field=models.DecimalField(max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='objectpost',
            name='Sex',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
    ]
