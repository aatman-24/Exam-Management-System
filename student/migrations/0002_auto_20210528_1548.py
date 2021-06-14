# Generated by Django 3.1.6 on 2021-05-28 10:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicprofile',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='academic', editable=False, populate_from='student', unique_with=('student',)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='student', unique_with=('student',)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='student', unique='student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='fullName', unique=True),
        ),
    ]
