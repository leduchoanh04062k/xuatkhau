# Generated by Django 4.2.6 on 2025-02-27 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_customuser_anh_bia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='zalo',
        ),
    ]
