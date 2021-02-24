# Generated by Django 2.2.13 on 2021-02-24 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_quiz_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='student',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='student',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='takenquiz',
            name='score',
        ),
        migrations.AddField(
            model_name='question',
            name='optionA',
            field=models.CharField(default='A şıkkı', max_length=255, verbose_name='OptionA'),
        ),
        migrations.AddField(
            model_name='question',
            name='optionB',
            field=models.CharField(default='B şıkkı', max_length=255, verbose_name='OptionB'),
        ),
        migrations.AddField(
            model_name='question',
            name='optionC',
            field=models.CharField(default='C şıkkı', max_length=255, verbose_name='OptionC'),
        ),
        migrations.AddField(
            model_name='question',
            name='optionD',
            field=models.CharField(default='D şıkkı', max_length=255, verbose_name='OptionD'),
        ),
        migrations.AddField(
            model_name='question',
            name='optionE',
            field=models.CharField(default='E şıkkı', max_length=255, verbose_name='OptionE'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 12, 0)),
        ),
        migrations.AddField(
            model_name='quiz',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 10, 0)),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
