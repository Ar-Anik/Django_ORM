# Generated by Django 4.0.2 on 2022-02-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(default='CSE-101', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='C Language', max_length=50, unique=True),
        ),
    ]
