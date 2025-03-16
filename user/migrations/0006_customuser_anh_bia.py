# Generated by Django 4.2.6 on 2025-02-26 14:06

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_avata'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='anh_bia',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='user', verbose_name='Ảnh bìa'),
        ),
    ]
