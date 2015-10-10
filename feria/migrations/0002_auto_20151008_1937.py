# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franquicia',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]
