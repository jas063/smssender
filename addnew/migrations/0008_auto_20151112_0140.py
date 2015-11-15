# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0007_auto_20151112_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sentto',
            new_name='sentTo',
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.IntegerField(default=1091),
            preserve_default=False,
        ),
    ]
