# Generated by Django 4.2.6 on 2025-02-28 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0030_alter_work_phi_xuat_canh'),
        ('user', '0012_alter_advisory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisory',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='advisory',
            name='path',
        ),
        migrations.AddField(
            model_name='advisory',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.work', verbose_name='Việc làm'),
        ),
    ]
