# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20141026_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'Project Category', choices=[(0, b'Unclassified'), (1, b'Building'), (2, b'Interior'), (3, b'Urban'), (4, b'Installation')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='subtype',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'Project Type', choices=[(0, b'Unclassified'), (1, b'Residential'), (2, b'Office'), (3, b'Cultural')]),
            preserve_default=True,
        ),
    ]
