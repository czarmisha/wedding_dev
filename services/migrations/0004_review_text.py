# Generated by Django 4.0 on 2021-12-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_review_delete_service_alter_accessories_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=' ', verbose_name='Текст отзыва'),
        ),
    ]