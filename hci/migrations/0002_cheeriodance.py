# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-06 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheerioDance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_url', models.CharField(max_length=512)),
            ],
        ),
    ]
