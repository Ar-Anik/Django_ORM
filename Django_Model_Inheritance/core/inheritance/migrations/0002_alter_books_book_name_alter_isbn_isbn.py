# Generated by Django 4.0.3 on 2022-03-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Book_Name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='isbn',
            name='Isbn',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]