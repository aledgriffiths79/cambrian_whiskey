# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-08-30 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=60)),
                ('message', models.TextField()),
            ],
        ),
    ]
