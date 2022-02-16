# Generated by Django 4.0 on 2022-02-16 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_videographer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='price_per_hour',
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(null=True, upload_to='portfolio/videos/%Y/%m/%d/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='services.portfolio')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
