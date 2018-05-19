# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grumblr', '0010_auto_20171007_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follow_list',
            field=models.ManyToManyField(related_name='follow_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
