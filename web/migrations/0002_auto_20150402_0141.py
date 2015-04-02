# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'sub categories'},
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, to='web.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(to='web.SubCategory', null=True),
            preserve_default=True,
        ),
    ]
