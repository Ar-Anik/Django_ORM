# Generated by Django 4.0.2 on 2022-02-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bangladeshi',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bangladeshi',
            name='Nid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='school_name',
            field=models.CharField(max_length=100),
        ),
    ]