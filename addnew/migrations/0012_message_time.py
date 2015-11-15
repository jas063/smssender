# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0011_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.CharField(default=datetime.datetime(2015, 11, 11, 21, 6, 16, 426000, tzinfo=utc), max_length=25),
            preserve_default=False,
        ),
    ]
