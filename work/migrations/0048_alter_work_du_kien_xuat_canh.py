# Generated by Django 4.2.6 on 2025-03-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0047_alter_work_du_kien_xuat_canh_alter_work_han_dang_ky'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='du_kien_xuat_canh',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dự kiến xuất cảnh'),
        ),
    ]
