# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_playbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TimeField()),
                ('action', models.CharField(max_length=255)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Host')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.AlterField(
            model_name='playbook',
            name='playbook',
            field=models.CharField(max_length=100),
        ),
    ]