# Generated by Django 2.1.5 on 2020-12-16 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0029_auto_20201216_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='pickup',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
