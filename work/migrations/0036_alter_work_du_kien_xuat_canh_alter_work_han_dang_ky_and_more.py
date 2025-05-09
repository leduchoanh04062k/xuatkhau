# Generated by Django 4.2.6 on 2025-03-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0035_alter_work_trinh_do_hoc_van'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='du_kien_xuat_canh',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dự kiến xuất cảnh'),
        ),
        migrations.AlterField(
            model_name='work',
            name='han_dang_ky',
            field=models.CharField(default=1, max_length=250, verbose_name='Hạn đăng ký'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work',
            name='hinh_thuc_thi_tuyen',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Hình thức thi tuyển'),
        ),
        migrations.AlterField(
            model_name='work',
            name='ngay_thi_tuyen',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ngày thi tuyển'),
        ),
    ]
