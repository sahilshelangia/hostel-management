# Generated by Django 2.2.1 on 2019-05-22 19:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatepass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('roll_no', models.CharField(blank=True, max_length=20, null=True)),
                ('mob_no', models.CharField(blank=True, max_length=11, null=True)),
                ('room_no', models.CharField(blank=True, max_length=3, null=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('hostel', models.CharField(max_length=5)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='gatepass_apply/pics')),
                ('from_date',
                 models.CharField(default=datetime.datetime(2019, 5, 22, 19, 27, 46, 636892), max_length=30)),
                (
                'to_date', models.CharField(default=datetime.datetime(2019, 5, 22, 19, 27, 46, 636929), max_length=30)),
                ('purpose', models.CharField(max_length=500)),
                ('address_during_leave', models.CharField(max_length=100)),
                ('hostel_supervisor',
                 models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
                                  default='Pending', max_length=20)),
                ('hostel_supervisor_remark', models.CharField(default='N/A', max_length=500)),
                ('hostel_warden',
                 models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
                                  default='Pending', max_length=20)),
                ('hostel_warden_remark', models.CharField(default='N/A', max_length=500)),
                ('hostel_assistant_warden',
                 models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
                                  default='Pending', max_length=20)),
                ('hostel_assistant_warden_remark', models.CharField(default='N/A', max_length=500)),
                ('control_room',
                 models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
                                  default='Pending', max_length=20)),
                ('control_room_remark', models.CharField(default='N/A', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=500)),
                ('quantity', models.CharField(max_length=3)),
                ('remark', models.CharField(max_length=500)),
                ('gatepass',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatepass_apply.Gatepass')),
            ],
        ),
    ]
