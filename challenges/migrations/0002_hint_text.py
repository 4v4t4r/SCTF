# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hint',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]