# Generated by Django 4.0 on 2022-04-19 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0042_accessories_phone2_accessories_phone3_agency_phone2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dress',
            name='dress_type',
        ),
    ]