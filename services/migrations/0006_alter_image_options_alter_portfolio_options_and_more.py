# Generated by Django 4.0 on 2022-01-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_portfolio_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Портфолио', 'verbose_name_plural': 'Портфолио'},
        ),
        migrations.AlterField(
            model_name='accessories',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='costume',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='dance',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='decor',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='dress',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='portfolio/images'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='music',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='photostudio',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='registryoffice',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='ring',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
    ]
