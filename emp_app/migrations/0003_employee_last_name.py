# Generated by Django 4.0.3 on 2022-04-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='Kumar', max_length=200),
        ),
    ]
