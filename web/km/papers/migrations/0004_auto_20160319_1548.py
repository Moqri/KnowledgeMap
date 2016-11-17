# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_paper_lsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='lsi',
            field=models.CharField(default=b'', max_length=500, null=True, blank=True),
        ),
    ]
