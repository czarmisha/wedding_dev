# Generated by Django 4.0 on 2022-02-16 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_remove_transport_price_per_hour_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photographer',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='videographer',
            old_name='full_name',
            new_name='name',
        ),
    ]
