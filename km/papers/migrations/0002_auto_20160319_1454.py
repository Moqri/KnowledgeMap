# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='cite',
            field=models.CharField(default=b'', max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='index',
            field=models.CharField(default=b'', max_length=10, null=True, blank=True),
        ),
    ]
