# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0010_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostManager',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]