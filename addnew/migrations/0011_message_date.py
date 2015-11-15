# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0010_remove_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.CharField(default=datetime.datetime(2015, 11, 11, 20, 57, 23, 881000, tzinfo=utc), max_length=25),
            preserve_default=False,
        ),
    ]
