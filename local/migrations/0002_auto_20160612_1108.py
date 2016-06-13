# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=200)),
                ('passwd', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
