# Generated by Django 4.2.6 on 2025-02-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0006_alter_province_country_alter_province_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='province',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='province',
            name='slug',
            field=models.SlugField(max_length=127),
        ),
        migrations.AddConstraint(
            model_name='province',
            constraint=models.UniqueConstraint(fields=('slug', 'country'), name='unique_slug_country'),
        ),
    ]
