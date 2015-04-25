# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(null=True, blank=True, upload_to='icons'),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to=web.models.Image.get_pictures_path),
        ),
    ]
