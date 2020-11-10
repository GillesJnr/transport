# Generated by Django 2.0 on 2020-11-10 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0005_auto_20201110_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='group_id',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_group', to='transport.VehicleGroup'),
        ),
    ]