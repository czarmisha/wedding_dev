# Generated by Django 4.0 on 2022-02-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_kitchentype_restaurant_kitchen'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]
