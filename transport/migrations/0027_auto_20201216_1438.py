# Generated by Django 2.1.5 on 2020-12-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0026_auto_20201216_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='transport.Users'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_booking', to='transport.Users'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_booking', to='transport.Vehicles'),
        ),
    ]