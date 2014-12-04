# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20141006_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subtype',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Project Type', choices=[(0, b'Unclassified'), (1, b'Residential'), (2, b'Office'), (3, b'Cultural')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.PositiveSmallIntegerField(verbose_name=b'Project Category', choices=[(0, b'Building'), (1, b'Interior'), (2, b'Urban'), (3, b'Installation')]),
            preserve_default=True,
        ),
    ]
