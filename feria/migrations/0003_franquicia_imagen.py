# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0002_auto_20151008_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='franquicia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'imagenes'),
        ),
    ]
