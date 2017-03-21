# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naverpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('urladdress', models.CharField(blank=True, max_length=120, null=True)),
                ('imageadress', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
