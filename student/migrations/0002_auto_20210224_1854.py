# Generated by Django 3.0 on 2021-02-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='diploma',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hsc_marks',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem1',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem2',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem3',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem4',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem5',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem6',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem7',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='sem8',
            field=models.FloatField(blank=True),
        ),
    ]