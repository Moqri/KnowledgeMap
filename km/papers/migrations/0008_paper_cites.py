# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0007_auto_20160325_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='cites',
            field=models.CharField(default=b'', max_length=10000, null=True, blank=True),
        ),
    ]
