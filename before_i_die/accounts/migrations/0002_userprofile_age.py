# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
