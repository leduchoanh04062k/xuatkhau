# Generated by Django 4.2.6 on 2025-02-26 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('city', '0005_alter_province_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='city.country'),
        ),
        migrations.AlterField(
            model_name='province',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provinces', to=settings.AUTH_USER_MODEL),
        ),
    ]
