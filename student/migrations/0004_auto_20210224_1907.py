# Generated by Django 3.0 on 2021-02-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210224_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='diploma_inst',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='diploma_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hsc_institute',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hsc_year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]