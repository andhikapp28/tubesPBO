# Generated by Django 3.0.8 on 2021-05-30 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210518_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gedung',
            name='MG',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Pegawai'),
        ),
    ]
