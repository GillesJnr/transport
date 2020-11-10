# Generated by Django 2.0 on 2020-11-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='vehicle_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]