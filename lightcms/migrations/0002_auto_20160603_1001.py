# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-03 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightcms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='block',
            unique_together=set([('title',)]),
        ),
    ]
