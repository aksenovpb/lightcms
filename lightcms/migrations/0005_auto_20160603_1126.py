# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-03 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightcms', '0004_auto_20160603_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='blocks',
        ),
        migrations.RemoveField(
            model_name='module',
            name='pages',
        ),
    ]
