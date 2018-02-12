# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_find_verbs', '0005_auto_20180211_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meaningexample',
            name='object_animacy',
        ),
        migrations.RemoveField(
            model_name='meaningexample',
            name='object_ref',
        ),
        migrations.RemoveField(
            model_name='meaningexample',
            name='purpose',
        ),
        migrations.AddField(
            model_name='meaning',
            name='object_animacy',
            field=models.CharField(blank=True, max_length=5, default='', choices=[('anim', 'одушевленный'), ('inan', 'неодушевленный'), ('noobj', 'безобъектное')]),
        ),
        migrations.AddField(
            model_name='meaning',
            name='object_ref',
            field=models.CharField(blank=True, max_length=10, default='', choices=[('ref_def', 'референтный определенный'), ('ref_indef', 'референтный неопределенный'), ('nonref', 'нереферентный'), ('abstr', 'абстрактный')]),
        ),
        migrations.AddField(
            model_name='meaning',
            name='purpose',
            field=models.CharField(blank=True, max_length=5, default='', choices=[('purp', 'умышленно'), ('byacc', 'случайно')]),
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='example',
            field=models.TextField(),
        ),
    ]
