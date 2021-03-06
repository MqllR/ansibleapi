# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('apikey', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='user',
            field=models.ManyToManyField(to='api.User'),
        ),
    ]
