# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0015_article_last_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['time']},
        ),
    ]
