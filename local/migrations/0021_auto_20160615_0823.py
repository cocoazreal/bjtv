# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0020_auto_20160612_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idsite', models.CharField(max_length=200)),
                ('ip', models.IntegerField()),
                ('pv', models.IntegerField()),
                ('uv', models.IntegerField()),
                ('datetime', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('week', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Statistics',
        ),
        migrations.AlterField(
            model_name='url',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
