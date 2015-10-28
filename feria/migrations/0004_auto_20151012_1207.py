# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0003_franquicia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franquicia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'imagenes', blank=True),
        ),
    ]
