# Generated by Django 2.1.5 on 2020-12-17 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0035_auto_20201217_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reasons',
            name='reasons_user',
        ),
    ]
