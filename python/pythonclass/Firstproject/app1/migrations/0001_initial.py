# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('mail_id', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
            ],
        ),
    ]