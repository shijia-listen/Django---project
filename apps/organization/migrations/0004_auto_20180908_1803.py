# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-08 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180908_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='student',
            new_name='students',
        ),
    ]