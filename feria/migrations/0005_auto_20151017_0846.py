# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feria', '0004_auto_20151012_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes')),
                ('activo', models.BooleanField(default=b'true')),
            ],
        ),
        migrations.AlterField(
            model_name='franquicia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'imagenes'),
        ),
        migrations.AddField(
            model_name='producto',
            name='franquicia',
            field=models.ForeignKey(to='feria.franquicia'),
        ),
    ]
