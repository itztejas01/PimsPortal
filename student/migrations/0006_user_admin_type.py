# Generated by Django 3.0 on 2021-07-21 04:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210302_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
