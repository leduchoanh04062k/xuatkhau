# Generated by Django 4.2.6 on 2025-02-26 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0017_alter_province_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Tỉnh, khu vực'},
        ),
    ]
