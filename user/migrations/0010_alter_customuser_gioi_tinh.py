# Generated by Django 4.2.6 on 2025-02-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_customuser_bang_nghe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gioi_tinh',
            field=models.CharField(blank=True, choices=[('Vui lòng chọn', 'Vui lòng chọn'), ('Nam', 'Nam'), ('Nữ', 'Nữ')], null=True, verbose_name='Giới tính'),
        ),
    ]
