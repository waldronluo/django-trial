# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privatesite', '0002_auto_20150119_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_list_item',
            name='content',
            field=models.TextField(),
        ),
    ]
