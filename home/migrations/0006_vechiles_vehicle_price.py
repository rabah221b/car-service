# Generated by Django 4.1 on 2022-09-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_vehicle_type_vechiles_vehicle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vechiles',
            name='vehicle_price',
            field=models.IntegerField(default=150),
        ),
    ]