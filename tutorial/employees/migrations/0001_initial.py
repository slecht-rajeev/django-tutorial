# Generated by Django 3.2.6 on 2021-08-18 21:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100, null=True)),
                ('employee_email', models.CharField(max_length=100, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 8, 19, 3, 8, 5, 947536))),
                ('employee_department', models.ForeignKey(blank=True, db_column='department_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.department')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]