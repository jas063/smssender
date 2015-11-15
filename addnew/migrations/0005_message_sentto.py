# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sentto',
            field=models.IntegerField(default=55555),
            preserve_default=False,
        ),
    ]
