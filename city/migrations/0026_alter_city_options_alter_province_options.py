# Generated by Django 4.2.6 on 2025-03-04 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0025_alter_city_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',), 'verbose_name_plural': 'Nơi thi tuyển'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ('priority',), 'verbose_name_plural': 'Tỉnh, khu vực'},
        ),
    ]
