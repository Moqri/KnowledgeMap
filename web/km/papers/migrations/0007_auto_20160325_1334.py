# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0006_auto_20160325_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='refs',
            field=models.CharField(default=b'', max_length=2000, null=True, blank=True),
        ),
    ]
