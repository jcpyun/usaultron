# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_policepost_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.DecimalField(max_digits=3, decimal_places=2)),
                ('Sex', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=200)),
                ('Relations', models.CharField(max_length=300)),
            ],
        ),
    ]
