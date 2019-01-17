# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nick01', '0005_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='state1',
            new_name='city1',
        ),
    ]
