# Generated by Django 2.2 on 2019-05-03 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('con_agg', '0004_auto_20190503_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitelist',
            name='header_type',
            field=models.CharField(default='h2', max_length=10),
        ),
        migrations.AlterField(
            model_name='content',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 20, 2, 42, 542174, tzinfo=utc)),
        ),
    ]