# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=520)),
                ('name', models.CharField(max_length=250)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
    ]
