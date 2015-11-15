# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0006_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='franquicia',
            name='modificado',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 13, 38, 28, 765083, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='modificado',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 13, 38, 50, 608430, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
