# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='easyGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='gameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warmth', models.CharField(max_length=200)),
                ('competence', models.CharField(max_length=200)),
                ('targets', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
