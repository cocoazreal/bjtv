# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0008_user_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passwd',
            new_name='passWd',
        ),
    ]
