# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150402_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('picture', models.ImageField(upload_to='get_pictures_path')),
                ('date', models.DateTimeField(null=True, auto_now_add=True)),
                ('product', models.ForeignKey(to='web.Product')),
            ],
        ),
    ]
