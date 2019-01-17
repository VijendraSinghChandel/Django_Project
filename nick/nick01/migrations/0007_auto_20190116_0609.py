# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nick01', '0006_auto_20190116_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='city1',
            field=models.ForeignKey(blank=True, to='nick01.City', null=True),
        ),
    ]
