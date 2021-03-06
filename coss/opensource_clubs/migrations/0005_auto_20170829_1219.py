# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('discourse', '0001_initial'),
        ('opensource_clubs', '0004_aboutpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('discourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='discourse.DiscourseCategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='categorylandingpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='categorylandingpage',
            name='discourse',
        ),
        migrations.AddField(
            model_name='categorylandingpage',
            name='heading',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='entitydetailpage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
