# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0005_auto_20171007_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
    ]
