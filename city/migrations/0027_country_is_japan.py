# Generated by Django 4.2.6 on 2025-03-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0026_alter_city_options_alter_province_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='is_japan',
            field=models.BooleanField(default=False),
        ),
    ]
