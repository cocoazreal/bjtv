# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 02:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0023_daydata_avg_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daydata',
            name='avg_ip',
        ),
    ]
