# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0006_auto_20160612_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
    ]