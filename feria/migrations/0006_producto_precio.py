# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0005_auto_20151017_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
