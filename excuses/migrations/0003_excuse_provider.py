# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excuses', '0002_auto_20150813_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='excuse',
            name='provider',
            field=models.CharField(max_length=50, default='DSW41923'),
            preserve_default=False,
        ),
    ]
