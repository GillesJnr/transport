# Generated by Django 2.1.5 on 2020-11-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0021_auto_20201118_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]