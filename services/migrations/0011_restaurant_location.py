# Generated by Django 4.0 on 2022-02-10 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_clientprofile_phone'),
        ('services', '0010_restaurant_facebook_restaurant_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
    ]