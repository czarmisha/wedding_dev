# Generated by Django 4.0 on 2021-12-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('client', 'Клиент'), ('specialist', 'Специалист'), ('other', 'Другой')], default='client', max_length=10, verbose_name='Тип пользователя'),
        ),
    ]
