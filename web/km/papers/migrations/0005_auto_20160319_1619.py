# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_auto_20160319_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='lsi',
            new_name='sim',
        ),
    ]
