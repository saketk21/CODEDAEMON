# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leader', '0015_cont_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cont_1',
            name='user',
        ),
        migrations.DeleteModel(
            name='cont_1',
        ),
    ]