# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
