# Generated by Django 2.1.5 on 2020-12-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0033_auto_20201216_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
