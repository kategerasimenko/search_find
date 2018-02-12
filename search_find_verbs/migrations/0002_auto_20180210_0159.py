# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_find_verbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='languageexample',
            name='field',
            field=models.ForeignKey(to='search_find_verbs.SemanticField', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meaningexample',
            name='field',
            field=models.ForeignKey(to='search_find_verbs.SemanticField', default=1),
            preserve_default=False,
        ),
    ]
