# Generated by Django 4.2.6 on 2025-02-26 12:18

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0020_rename_quoc_gia_province_country'),
        ('work', '0017_alter_work_country_alter_work_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='country', chained_model_field='country', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_id', to='city.province', verbose_name='Tỉnh, khu vực'),
        ),
    ]
