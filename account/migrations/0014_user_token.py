# Generated by Django 4.0 on 2022-06-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_district_name_uz'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Email Token'),
        ),
    ]
