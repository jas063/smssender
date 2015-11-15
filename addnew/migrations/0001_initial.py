# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=25)),
                ('mobile', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('mariage_aniversary', models.DateField()),
                ('remarks', models.CharField(max_length=100, blank=True)),
            ],
        ),
    ]
