# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0008_auto_20151112_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
