# Generated by Django 4.0.5 on 2022-06-05 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_complete_date_alter_note_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='complete_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 6, 12, 51, 10, 191977, tzinfo=utc), verbose_name='Время выполнения'),
        ),
        migrations.AlterField(
            model_name='note',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 5, 12, 51, 10, 191977, tzinfo=utc), verbose_name='Время создания'),
        ),
    ]
