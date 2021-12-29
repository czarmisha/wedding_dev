# Generated by Django 4.0 on 2021-12-29 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_clientprofile_avatar'),
        ('services', '0002_transport_stylist_ring_restaurant_registryoffice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='account.user')),
                ('service_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_reviews', to='account.user')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AlterModelOptions(
            name='accessories',
            options={'verbose_name': 'Свадебные аксессуары', 'verbose_name_plural': 'Свадебные аксессуары'},
        ),
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name': 'Свадебное агенство', 'verbose_name_plural': 'Свадебные агенства'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Шоу программа, артист', 'verbose_name_plural': 'Шоу программы, артисты'},
        ),
        migrations.AlterModelOptions(
            name='bouquet',
            options={'verbose_name': 'Свадебный букет', 'verbose_name_plural': 'Свадебные букеты'},
        ),
        migrations.AlterModelOptions(
            name='cake',
            options={'verbose_name': 'Свадебный торт', 'verbose_name_plural': 'Свадебные торты'},
        ),
        migrations.AlterModelOptions(
            name='costume',
            options={'verbose_name': 'Свадебный костюм', 'verbose_name_plural': 'Свадебные костюмы'},
        ),
        migrations.AlterModelOptions(
            name='dance',
            options={'verbose_name': 'Свадебный танец', 'verbose_name_plural': 'Свадебный танец'},
        ),
        migrations.AlterModelOptions(
            name='decor',
            options={'verbose_name': 'Оформление и декор', 'verbose_name_plural': 'Оформление и декор'},
        ),
        migrations.AlterModelOptions(
            name='dress',
            options={'verbose_name': 'Свадебное платье', 'verbose_name_plural': 'Свадебные платья'},
        ),
        migrations.AlterModelOptions(
            name='invitation',
            options={'verbose_name': 'Пригласительное', 'verbose_name_plural': 'Пригласительные'},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': 'Музыкальная группа, DJ', 'verbose_name_plural': 'Музыкальные группы, DJ'},
        ),
        migrations.AlterModelOptions(
            name='photographer',
            options={'verbose_name': 'Фотограф', 'verbose_name_plural': 'Фотографы'},
        ),
        migrations.AlterModelOptions(
            name='photostudio',
            options={'verbose_name': 'Фотостудия', 'verbose_name_plural': 'Фотостудии'},
        ),
        migrations.AlterModelOptions(
            name='presenter',
            options={'verbose_name': 'Ведущий', 'verbose_name_plural': 'Ведущие'},
        ),
        migrations.AlterModelOptions(
            name='registryoffice',
            options={'verbose_name': 'Дворец бракосочетания, ЗАГС', 'verbose_name_plural': 'Дворцы бракосочтания, ЗАГСы'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Банкетный зал, ретсоран', 'verbose_name_plural': 'Банкетные залы, рестораны'},
        ),
        migrations.AlterModelOptions(
            name='ring',
            options={'verbose_name': 'Свадебное кольцо', 'verbose_name_plural': 'Свадебные кольца'},
        ),
        migrations.AlterModelOptions(
            name='stylist',
            options={'verbose_name': 'Стилист, визажист', 'verbose_name_plural': 'Стилисты, визажисты'},
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'verbose_name': 'Транспорт', 'verbose_name_plural': 'Транспорт'},
        ),
        migrations.AlterField(
            model_name='accessories',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/accessories', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/agencies', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/artists', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/bouquets', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/cakes', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='costume',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/costumes', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='dance',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/dances', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='decor',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/decors', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='dress',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/dresses', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/invitations', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='music',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/musician', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/photographers', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='photostudio',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/photoStudios', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/presenters', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='registryoffice',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/registryOffices', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/restaurants', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='ring',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/rings', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/stylists', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/transports', verbose_name='Аватар'),
        ),
    ]