# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_find_verbs', '0006_auto_20180212_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='semanticfield',
            name='comments',
            field=models.TextField(blank=True, default=''),
        ),
    ]
