# Generated by Django 3.1.6 on 2021-05-28 10:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='student', unique_with=('student', 'exam')),
        ),
    ]