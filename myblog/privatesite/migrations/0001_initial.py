# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='p_block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='p_list_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=512)),
                ('beginDate', models.DateField()),
                ('endDate', models.DateField()),
                ('block', models.ForeignKey(related_name='block_belonged', to='privatesite.p_block')),
            ],
        ),
    ]
