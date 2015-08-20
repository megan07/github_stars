# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('num_stars', models.IntegerField()),
                ('num_watchers', models.IntegerField()),
                ('num_forks', models.IntegerField()),
            ],
        ),
    ]
