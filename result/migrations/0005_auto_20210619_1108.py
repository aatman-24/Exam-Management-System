# Generated by Django 3.1.6 on 2021-06-19 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20210608_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['-publishedDate'], 'permissions': (('publish_result', 'Can publish results'),)},
        ),
    ]