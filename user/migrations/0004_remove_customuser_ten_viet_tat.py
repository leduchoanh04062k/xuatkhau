# Generated by Django 4.2.6 on 2025-02-26 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_chuc_vu_customuser_kinh_nghiem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ten_viet_tat',
        ),
    ]
