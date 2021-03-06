# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-13 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hci', '0005_delete_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('baseball_k', models.CharField(max_length=20)),
                ('baseball_y', models.CharField(max_length=20)),
                ('baseball_r', models.CharField(max_length=20)),
                ('baseketball_k', models.CharField(max_length=20)),
                ('baseketball_y', models.CharField(max_length=20)),
                ('baseketball_r', models.CharField(max_length=20)),
                ('ice_k', models.CharField(max_length=20)),
                ('ice_y', models.CharField(max_length=20)),
                ('ice_r', models.CharField(max_length=20)),
                ('football_k', models.CharField(max_length=20)),
                ('football_y', models.CharField(max_length=20)),
                ('football_r', models.CharField(max_length=20)),
                ('soccer_k', models.CharField(max_length=20)),
                ('soccer_y', models.CharField(max_length=20)),
                ('soccer_r', models.CharField(max_length=20)),
                ('total_k', models.CharField(max_length=20)),
                ('total_tie', models.CharField(max_length=20)),
                ('total_y', models.CharField(max_length=20)),
                ('total_r', models.CharField(max_length=20)),
            ],
        ),
    ]
