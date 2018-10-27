# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='value',
        ),
        migrations.AddField(
            model_name='app',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000, verbose_name='name'),
            preserve_default=False,
        ),
    ]
