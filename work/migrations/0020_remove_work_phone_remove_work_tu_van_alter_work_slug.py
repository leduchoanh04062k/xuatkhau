# Generated by Django 4.2.6 on 2025-02-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0019_remove_work_ma_don_hang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='work',
            name='tu_van',
        ),
        migrations.AlterField(
            model_name='work',
            name='slug',
            field=models.SlugField(blank=True, max_length=127, unique=True),
        ),
    ]
