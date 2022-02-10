# Generated by Django 4.0 on 2022-02-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_restaurant_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantAdditionalFeeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название услуги')),
            ],
            options={
                'verbose_name': 'Услуга за доп плату',
                'verbose_name_plural': 'Услуги за доп плату',
            },
        ),
        migrations.CreateModel(
            name='RestaurantBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Преимущество заведения',
                'verbose_name_plural': 'Преимущества заведения',
            },
        ),
        migrations.CreateModel(
            name='RestaurantPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Способ оплаты',
                'verbose_name_plural': 'Способы оплаты',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='additional_services',
            field=models.ManyToManyField(to='services.RestaurantAdditionalFeeService', verbose_name='Услуги за доп плату'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='benefits',
            field=models.ManyToManyField(to='services.RestaurantBenefits', verbose_name='Преимущества'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='payment',
            field=models.ManyToManyField(to='services.RestaurantPaymentMethod', verbose_name='Способы оплаты'),
        ),
    ]