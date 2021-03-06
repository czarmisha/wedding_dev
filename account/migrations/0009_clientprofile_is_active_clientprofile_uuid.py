# Generated by Django 4.0 on 2022-05-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is active'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='uuid',
            field=models.SlugField(blank=True, max_length=120, null=True, unique=True, verbose_name='User unique ID'),
        ),
    ]
