# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=8)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=256)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
