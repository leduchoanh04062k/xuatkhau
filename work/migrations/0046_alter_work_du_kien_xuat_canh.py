# Generated by Django 4.2.6 on 2025-03-05 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0045_alter_work_du_kien_xuat_canh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='du_kien_xuat_canh',
            field=models.DateField(default=datetime.date.today, verbose_name='Dự kiến xuất cảnh'),
        ),
    ]
