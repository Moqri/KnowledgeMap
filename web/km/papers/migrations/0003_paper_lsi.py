# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20160319_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='lsi',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
    ]
