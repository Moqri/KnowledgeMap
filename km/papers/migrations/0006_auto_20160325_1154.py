# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20160319_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='wom',
        ),
        migrations.AddField(
            model_name='paper',
            name='doi',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='refs',
            field=models.CharField(default=b'', max_length=1000, null=True, blank=True),
        ),
    ]
