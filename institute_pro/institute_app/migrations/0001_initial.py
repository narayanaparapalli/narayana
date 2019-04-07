# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-06 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstContact_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('cources', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'Python'), ('dj', 'django'), ('UI', 'UI'), ('api', 'Rest API')], max_length=200)),
                ('locations', multiselectfield.db.fields.MultiSelectField(choices=[('hyd', 'Hyderabad'), ('bang', 'Bangalore'), ('pune', 'Pune'), ('chenni', 'chenni')], max_length=200)),
                ('shifts', multiselectfield.db.fields.MultiSelectField(choices=[('mng', 'Morning'), ('aftnoon', 'Afternoon'), ('evng', 'Evining'), ('night', 'night')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InstFeedback_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateField()),
                ('feedback', models.TextField(max_length=1000)),
            ],
        ),
    ]