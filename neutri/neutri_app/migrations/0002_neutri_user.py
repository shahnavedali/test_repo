# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neutri_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neutri_User',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
