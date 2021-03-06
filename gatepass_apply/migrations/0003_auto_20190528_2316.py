# Generated by Django 2.1.7 on 2019-05-28 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gatepass_apply', '0002_auto_20190525_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatepass',
            name='applied_on',
            field=models.CharField(default=datetime.datetime(2019, 5, 28, 23, 16, 26, 26024), max_length=30),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='from_date',
            field=models.CharField(default=datetime.datetime(2019, 5, 28, 23, 16, 26, 26024), max_length=30),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='to_date',
            field=models.CharField(default=datetime.datetime(2019, 5, 28, 23, 16, 26, 26024), max_length=30),
        ),
    ]
