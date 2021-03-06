# Generated by Django 4.0 on 2022-02-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_restauranttype_alter_accessories_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название кухни')),
            ],
            options={
                'verbose_name': 'Кухня',
                'verbose_name_plural': 'Кухни',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='kitchen',
            field=models.ManyToManyField(to='services.KitchenType', verbose_name='Кухня'),
        ),
    ]
