# Generated by Django 3.0 on 2021-03-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210224_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
