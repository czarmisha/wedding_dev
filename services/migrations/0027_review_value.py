# Generated by Django 4.0 on 2022-02-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_alter_transport_with_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Значение оценки'),
        ),
    ]