# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='user_likes', to='blog.Like'),
        ),
    ]
