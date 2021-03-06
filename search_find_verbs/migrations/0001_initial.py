# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-09 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example', models.TextField(blank=True, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_find_verbs.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeaningExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=200)),
                ('example', models.TextField()),
                ('meaning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_find_verbs.Meaning')),
            ],
        ),
        migrations.CreateModel(
            name='MeaningType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SemanticField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_find_verbs.Language')),
            ],
        ),
        migrations.AddField(
            model_name='meaning',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_find_verbs.SemanticField'),
        ),
        migrations.AddField(
            model_name='meaning',
            name='meaning_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_find_verbs.MeaningType'),
        ),
        migrations.AddField(
            model_name='languageexample',
            name='meaning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_find_verbs.MeaningExample'),
        ),
        migrations.AddField(
            model_name='languageexample',
            name='verbs',
            field=models.ManyToManyField(to='search_find_verbs.Verb'),
        ),
    ]
