# Generated by Django 4.0 on 2022-02-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0006_alter_response_options_alter_tender_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='service',
            field=models.CharField(choices=[('photographer', 'Фотограф'), ('artist', 'Артист, Шоу программа'), ('transport', 'Транспорт'), ('music', 'Музыканты, Dj'), ('presenter', 'Ведущий'), ('invitation', 'Пригласительные'), ('cake', 'Торт'), ('dress', 'Платье'), ('ring', 'Кольца'), ('bouquet', 'Букет'), ('decor', 'Декор, оформление'), ('costume', 'Костюм'), ('accessories', 'Аксуссуары'), ('stylist', 'Стилист, Визажист'), ('photostudio', 'Фотостудия'), ('dance', 'Танец'), ('agency', 'Агенство'), ('videographer', 'Видеограф')], default=None, max_length=15),
        ),
    ]