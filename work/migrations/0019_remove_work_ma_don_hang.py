# Generated by Django 4.2.6 on 2025-02-26 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0018_alter_work_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='ma_don_hang',
        ),
    ]
