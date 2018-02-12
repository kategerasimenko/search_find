# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_find_verbs', '0003_auto_20180211_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageexample',
            name='example',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='example',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='object_animacy',
            field=models.CharField(choices=[('anim', 'одушевленный'), ('inan', 'неодушевленный'), ('noobj', 'безобъектное')], blank=True, max_length=4, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='object_ref',
            field=models.CharField(choices=[('ref_def', 'референтный определенный'), ('ref_indef', 'референтный неопределенный'), ('nonref', 'нереферентный'), ('abstr', 'абстрактный')], blank=True, max_length=10, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='purpose',
            field=models.CharField(choices=[('purp', 'умышленно'), ('byacc', 'случайно')], blank=True, max_length=5, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meaningexample',
            name='specification',
            field=models.CharField(default='', blank=True, max_length=200),
            preserve_default=False,
        ),
    ]
