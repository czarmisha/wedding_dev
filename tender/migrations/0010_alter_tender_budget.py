# Generated by Django 4.0 on 2022-03-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0009_alter_tender_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='budget',
            field=models.IntegerField(verbose_name='Бюджет (y.e.)'),
        ),
    ]
