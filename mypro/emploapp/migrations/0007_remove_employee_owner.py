# Generated by Django 3.2.9 on 2021-11-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emploapp', '0006_employee_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='owner',
        ),
    ]