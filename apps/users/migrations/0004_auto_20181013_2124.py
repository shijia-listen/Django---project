# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-13 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181001_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de\u5bc6\u7801'), ('update_email', '\u4fee\u6539\u90ae\u7bb1')], max_length=30, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b'),
        ),
    ]
