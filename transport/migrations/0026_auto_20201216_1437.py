# Generated by Django 2.1.5 on 2020-12-16 14:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0025_auto_20201215_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='transport.Users'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_booking', to='transport.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookings',
            name='payment',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='travellers',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_booking', to='transport.Vehicles'),
            preserve_default=False,
        ),
    ]
