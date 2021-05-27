# Generated by Django 3.1.6 on 2021-05-27 13:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(choices=[('English', 'English'), ('Physic', 'Physic'), ('Chemistry', 'Chemistry'), ('Maths', 'Maths'), ('Biology', 'Biology'), ('Computer', 'Computer'), ('JEE-Maths', 'JEE-Maths'), ('JEE-Physic', 'JEE-Physic'), ('JEE-Chemistry', 'JEE-Chemistry'), ('NEET-Biology', 'NEET-Biology'), ('NEET-Physic', 'NEET-Physic'), ('NEET-Chemistry', 'NEET-Chemistry')], max_length=20, verbose_name='Subject Name')),
                ('standard', models.PositiveIntegerField(default=11, validators=[django.core.validators.MinValueValidator(11), django.core.validators.MaxValueValidator(12)], verbose_name='Standard')),
                ('totalMarks', models.IntegerField(default=0, verbose_name='Total Exam Marks')),
                ('totalExam', models.IntegerField(default=0, verbose_name='Total Exam')),
                ('currentYear', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(help_text='A label for URL config.', unique=True)),
            ],
            options={
                'unique_together': {('currentYear', 'subjectName', 'standard')},
            },
        ),
        migrations.CreateModel(
            name='SubjectExamRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalMarks', models.IntegerField(default=0, verbose_name='Subject Total Marks')),
                ('totalExam', models.IntegerField(default=0, verbose_name='Subject Total Exam')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_record', to='study.subject')),
            ],
        ),
    ]
