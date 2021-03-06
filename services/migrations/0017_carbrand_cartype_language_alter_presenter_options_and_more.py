# Generated by Django 4.0 on 2022-02-11 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_clientprofile_phone'),
        ('services', '0016_registryoffice_facebook_registryoffice_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Марка автомобиля',
                'verbose_name_plural': 'Марки автомобилей',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип автомобиля',
                'verbose_name_plural': 'Типы автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.AlterModelOptions(
            name='presenter',
            options={'ordering': ['-is_pro', '-created'], 'verbose_name': 'Ведущий и тамада', 'verbose_name_plural': 'Ведущие и тамада'},
        ),
        migrations.RemoveField(
            model_name='photostudio',
            name='price',
        ),
        migrations.AddField(
            model_name='decor',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='decor',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='decor',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='decor',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='decor',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='photostudio',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='photostudio',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='photostudio',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='photostudio',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='presenter',
            name='composition',
            field=models.CharField(choices=[('duet', 'Дуэт'), ('solo', 'Соло')], max_length=50, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='presenter',
            name='gender',
            field=models.CharField(choices=[('men', 'Мужчина'), ('women', 'Женщина'), ('mixed', 'Смешанный')], max_length=50, null=True, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='presenter',
            name='price_per_evening',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='transport',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='transport',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='transport',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='transport',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='transport',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='presenter',
            name='language',
            field=models.ManyToManyField(to='services.Language', verbose_name='Языки'),
        ),
        migrations.AddField(
            model_name='transport',
            name='car_brand',
            field=models.ManyToManyField(to='services.CarBrand', verbose_name='Марка автомобиля'),
        ),
        migrations.AddField(
            model_name='transport',
            name='car_type',
            field=models.ManyToManyField(to='services.CarType', verbose_name='Тип автомобиля'),
        ),
    ]
