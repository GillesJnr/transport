# Generated by Django 2.1.5 on 2020-11-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0006_auto_20201124_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='custom_type',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='vendors_user',
        ),
    ]
