# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nick01', '0003_city_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.AddField(
            model_name='city',
            name='state1',
            field=models.ForeignKey(blank=True, to='nick01.State', null=True),
        ),
    ]
