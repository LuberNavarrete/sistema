# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0007_auto_20151115_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='franquicia',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 13, 39, 45, 152610, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 13, 39, 47, 821549, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
