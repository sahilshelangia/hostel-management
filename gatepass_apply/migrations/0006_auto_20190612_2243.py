# Generated by Django 2.1.7 on 2019-06-12 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gatepass_apply', '0005_auto_20190530_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepass',
            name='from_date',
            field=models.CharField(default=datetime.datetime(2019, 6, 12, 22, 43, 2, 367845), max_length=30),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='to_date',
            field=models.CharField(default=datetime.datetime(2019, 6, 12, 22, 43, 2, 367845), max_length=30),
        ),
    ]
