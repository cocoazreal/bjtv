# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0013_auto_20160612_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='date',
            field=models.DateTimeField(blank=True, default='0000 00 00 00:00:00'),
        ),
    ]