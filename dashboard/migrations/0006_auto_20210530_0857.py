# Generated by Django 3.0.8 on 2021-05-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210530_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gedung',
            name='MG_Gedung',
        ),
        migrations.AddField(
            model_name='gedung',
            name='MG',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
