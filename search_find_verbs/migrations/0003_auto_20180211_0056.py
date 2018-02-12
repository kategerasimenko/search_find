# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_find_verbs', '0002_auto_20180210_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meaning',
            name='field',
        ),
        migrations.AddField(
            model_name='meaningexample',
            name='object_animacy',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[('anim', 'одушевленный'), ('inan', 'неодушевленный')]),
        ),
        migrations.AddField(
            model_name='meaningexample',
            name='object_ref',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[('ref_def', 'референтный определенный'), ('ref_indef', 'референтный неопределенный'), ('nonref', 'нереферентный'), ('abstr', 'абстрактный')]),
        ),
        migrations.AddField(
            model_name='meaningexample',
            name='purpose',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[('purp', 'умышленно'), ('byacc', 'случайно')]),
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='specification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
