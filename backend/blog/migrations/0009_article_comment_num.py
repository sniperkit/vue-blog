# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_child_reply_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
    ]
