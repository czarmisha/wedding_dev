# Generated by Django 4.0 on 2022-02-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_stylist_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='with_driver',
            field=models.CharField(choices=[('1', 'С водителем'), ('2', 'Без водителя')], max_length=50, null=True),
        ),
    ]
