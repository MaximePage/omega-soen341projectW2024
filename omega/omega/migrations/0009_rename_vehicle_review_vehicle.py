# Generated by Django 5.0.1 on 2024-04-07 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omega', '0008_review_vehicle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Vehicle',
            new_name='vehicle',
        ),
    ]
