# Generated by Django 4.0 on 2021-12-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_clientprofile_options_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/clients', verbose_name='Аватар'),
        ),
    ]
