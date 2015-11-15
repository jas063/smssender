# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addnew', '0002_auto_20151104_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add',
            old_name='mariage_aniversary',
            new_name='marriageaniversary',
        ),
    ]
