# Generated by Django 4.2.6 on 2025-02-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0029_alter_work_chuyen_nganh_alter_work_hop_dong_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='phi_xuat_canh',
            field=models.CharField(blank=True, null=True, verbose_name='Phí xuất cảnh'),
        ),
    ]
