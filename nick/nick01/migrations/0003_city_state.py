# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nick01', '0002_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
