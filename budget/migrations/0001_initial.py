# Generated by Django 4.0 on 2022-01-24 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0007_alter_clientprofile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_json', models.JSONField(blank=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='budget', to='account.user')),
            ],
            options={
                'verbose_name': 'Свадебный Бюджет',
            },
        ),
    ]
