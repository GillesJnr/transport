# Generated by Django 2.1.5 on 2020-12-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0030_auto_20201216_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='pickup',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
