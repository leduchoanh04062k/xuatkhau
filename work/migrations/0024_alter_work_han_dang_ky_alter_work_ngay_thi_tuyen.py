# Generated by Django 4.2.6 on 2025-02-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0023_alter_work_quyen_loi_khac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='han_dang_ky',
            field=models.DateField(default=0, verbose_name='Hạn đăng ký'),
        ),
        migrations.AlterField(
            model_name='work',
            name='ngay_thi_tuyen',
            field=models.DateField(default=0, verbose_name='Ngày thi tuyển'),
        ),
    ]
