# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_find_verbs', '0004_auto_20180211_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meaningexample',
            name='object_animacy',
            field=models.CharField(blank=True, choices=[('anim', 'одушевленный'), ('inan', 'неодушевленный'), ('noobj', 'безобъектное')], max_length=5),
        ),
    ]
