# Generated by Django 2.1.5 on 2020-11-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0007_auto_20201126_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
