# Generated by Django 5.0.1 on 2024-03-11 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omega', '0002_rename_vehicle_id_reservation_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_price',
        ),
    ]
