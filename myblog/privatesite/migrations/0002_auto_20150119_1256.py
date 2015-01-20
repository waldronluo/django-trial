# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privatesite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_list_item',
            name='address',
            field=models.CharField(default='SYSU', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p_list_item',
            name='name',
            field=models.CharField(default='Developer', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='p_list_item',
            name='content',
            field=models.CharField(max_length=1024),
        ),
    ]
