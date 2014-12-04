# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['embed_project_order']},
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.PositiveSmallIntegerField(verbose_name=b'Project Type', choices=[(0, b'Unclassified'), (1, b'Residential'), (2, b'Office'), (3, b'Public'), (4, b'Urban Design'), (5, b'Land Scape'), (6, b'Manufacture')]),
        ),
    ]
