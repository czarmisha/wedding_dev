# Generated by Django 4.0 on 2022-02-11 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_clientprofile_phone'),
        ('services', '0017_carbrand_cartype_language_alter_presenter_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoriesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип аксессуаров',
                'verbose_name_plural': 'Типы аксессуаров',
            },
        ),
        migrations.CreateModel(
            name='ShowType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип шоупрограммы',
                'verbose_name_plural': 'Типы шоупрограмм',
            },
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-is_pro', '-created'], 'verbose_name': 'Музыкальная группа и DJ', 'verbose_name_plural': 'Музыкальные группы и DJ'},
        ),
        migrations.RemoveField(
            model_name='music',
            name='price_per_hour',
        ),
        migrations.AddField(
            model_name='accessories',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='accessories',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='accessories',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='agency',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='agency',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='agency',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='agency',
            name='price',
            field=models.FloatField(null=True, verbose_name='Начальная цена'),
        ),
        migrations.AddField(
            model_name='agency',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='artist',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='artist',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='artist',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cake',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='cake',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='cake',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='cake',
            name='price',
            field=models.FloatField(null=True, verbose_name='Начальная цена'),
        ),
        migrations.AddField(
            model_name='cake',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='cake',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='costume',
            name='condition',
            field=models.CharField(choices=[('sale', 'Продажа'), ('rent', 'Аренд')], max_length=50, null=True, verbose_name='Вид сделки'),
        ),
        migrations.AddField(
            model_name='costume',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='costume',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='costume',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='costume',
            name='price',
            field=models.FloatField(null=True, verbose_name='Начальная цена'),
        ),
        migrations.AddField(
            model_name='costume',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='costume',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dance',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='dance',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='dance',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='dance',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='dance',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dress',
            name='condition',
            field=models.CharField(choices=[('sale', 'Продажа'), ('rent', 'Аренд')], max_length=50, null=True, verbose_name='Вид сделки'),
        ),
        migrations.AddField(
            model_name='dress',
            name='dress_type',
            field=models.CharField(choices=[('bouffant', 'Пышное'), ('straight', 'Прямое')], max_length=50, null=True, verbose_name='Тип платье'),
        ),
        migrations.AddField(
            model_name='dress',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='dress',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='dress',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='dress',
            name='price',
            field=models.FloatField(null=True, verbose_name='Начальная цена'),
        ),
        migrations.AddField(
            model_name='dress',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='dress',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invitation',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='invitation',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='invitation',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='price',
            field=models.FloatField(null=True, verbose_name='Начальная цена'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='music',
            name='composition',
            field=models.CharField(choices=[('duet', 'Дуэт'), ('solo', 'Соло'), ('group', 'Группа'), ('dj', 'Dj')], max_length=50, null=True, verbose_name='Исполнители'),
        ),
        migrations.AddField(
            model_name='music',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='music',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='music',
            name='language',
            field=models.ManyToManyField(to='services.Language', verbose_name='Языки исполнения песен'),
        ),
        migrations.AddField(
            model_name='music',
            name='price_per_evening',
            field=models.FloatField(null=True, verbose_name='Цена за вечер'),
        ),
        migrations.AddField(
            model_name='music',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='music',
            name='vocal',
            field=models.CharField(choices=[('men', 'Мужской'), ('women', 'Женский'), ('mixed', 'Смешанный')], max_length=50, null=True, verbose_name='Вокал'),
        ),
        migrations.AddField(
            model_name='presenter',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='presenter',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='presenter',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='ring',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='ring',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='ring',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='ring',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='ring',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='ring',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stylist',
            name='facebook',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='stylist',
            name='instagram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='stylist',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='stylist',
            name='telegram',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='stylist',
            name='type',
            field=models.CharField(choices=[('business', 'Компания'), ('private', 'Индивидуальные услуги')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='price_per_kg',
            field=models.FloatField(null=True, verbose_name='Цена за кг'),
        ),
        migrations.AlterField(
            model_name='dance',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена '),
        ),
        migrations.AlterField(
            model_name='music',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='price_per_hour',
            field=models.FloatField(null=True, verbose_name='Цена за час'),
        ),
        migrations.AlterField(
            model_name='photostudio',
            name='price_per_hour',
            field=models.FloatField(null=True, verbose_name='Цена за час'),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена '),
        ),
        migrations.AlterField(
            model_name='transport',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='price_per_hour',
            field=models.FloatField(null=True, verbose_name='Цена за час'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='accessories_type',
            field=models.ManyToManyField(null=True, to='services.AccessoriesType'),
        ),
        migrations.AddField(
            model_name='artist',
            name='type',
            field=models.ManyToManyField(null=True, to='services.ShowType', verbose_name='Тип шоупрограммы'),
        ),
    ]
