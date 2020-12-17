# Generated by Django 2.1.5 on 2020-12-16 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0031_auto_20201216_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuel',
            name='fuel_user',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='vehicle_id',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='vendor_name',
        ),
        migrations.AddField(
            model_name='fuel',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_fuel', to='transport.Vehicles'),
        ),
        migrations.AddField(
            model_name='fuel',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuel_vendor', to='transport.Vendors'),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='complete',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='cost_per_unit',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='qty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]