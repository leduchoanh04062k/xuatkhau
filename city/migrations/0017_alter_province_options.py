# Generated by Django 4.2.6 on 2025-02-26 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0016_remove_province_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ('id',), 'verbose_name_plural': 'Tỉnh, khu vực'},
        ),
    ]
