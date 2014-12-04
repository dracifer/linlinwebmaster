# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('embed_project_text', models.TextField()),
                ('embed_project_order', models.PositiveSmallIntegerField()),
                ('data', models.ImageField(upload_to=b'images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=256)),
                ('category', models.PositiveSmallIntegerField(choices=[(0, b'Unclassified'), (1, b'Residential'), (2, b'Office'), (3, b'Public'), (4, b'Urban Design'), (5, b'Land Scape'), (6, b'Manufacture')])),
                ('scale', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('note', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, b'Not Started'), (1, b'Researching'), (2, b'In Progress'), (3, b'Suspended'), (4, b'Completed'), (5, b'Aborted')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(default=b'Anonymous', max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=128)),
                ('group', models.ForeignKey(to='projects.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='projects.User'),
            preserve_default=True,
        ),
    ]
