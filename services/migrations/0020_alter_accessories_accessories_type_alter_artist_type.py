# Generated by Django 4.0 on 2022-02-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_remove_presenter_price_per_evening_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='accessories_type',
            field=models.ManyToManyField(to='services.AccessoriesType'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='type',
            field=models.ManyToManyField(to='services.ShowType', verbose_name='Тип шоупрограммы'),
        ),
    ]