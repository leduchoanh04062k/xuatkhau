# Generated by Django 4.2.6 on 2025-03-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=127, null=True),
        ),
    ]
