# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 23:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20170724_1513'),
        ('home', '0018_auto_20171005_2013'),
        ('Leader', '0052_cont_5_sub_cont_5'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_time', models.DateTimeField(blank=True)),
                ('tot_score', models.IntegerField(default=0)),
                ('Reverse_Coding_1', models.IntegerField(default=0)),
                ('Reverse_Coding_2', models.IntegerField(default=0)),
                ('Number_Conversion', models.IntegerField(default=0)),
                ('Debugger', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'ordering': ['-tot_score', 'sub_time'],
            },
        ),
        migrations.CreateModel(
            name='Sub_cont_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('time', models.DateTimeField()),
                ('Lang', models.CharField(max_length=10)),
                ('pts', models.IntegerField(default=0)),
                ('res', models.CharField(max_length=100)),
                ('Problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problem')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
