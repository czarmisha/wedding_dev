# Generated by Django 4.0 on 2022-02-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_accessoriestype_showtype_alter_music_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenter',
            name='price_per_evening',
        ),
        migrations.AddField(
            model_name='presenter',
            name='price_per_hour',
            field=models.FloatField(null=True, verbose_name='Цена за час'),
        ),
        migrations.AlterField(
            model_name='decor',
            name='price',
            field=models.FloatField(null=True, verbose_name='Минимальная цена украшения зала'),
        ),
        migrations.AlterField(
            model_name='music',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена за выступление'),
        ),
    ]
