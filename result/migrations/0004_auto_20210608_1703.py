# Generated by Django 3.1.6 on 2021-06-08 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_auto_20210528_1548'),
        ('student', '0003_auto_20210528_1620'),
        ('result', '0003_auto_20210528_1620'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'exam')},
        ),
    ]
