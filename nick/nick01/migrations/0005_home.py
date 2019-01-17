# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nick01', '0004_auto_20190112_0544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ownername', models.CharField(max_length=500)),
                ('HomeNO', models.IntegerField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=50, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('state1', models.ForeignKey(blank=True, to='nick01.State', null=True)),
            ],
        ),
    ]
