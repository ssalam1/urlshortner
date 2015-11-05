# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
