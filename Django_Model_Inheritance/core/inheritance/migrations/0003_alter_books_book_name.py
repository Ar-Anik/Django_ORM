# Generated by Django 4.0.3 on 2022-03-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0002_alter_books_book_name_alter_isbn_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Book_Name',
            field=models.CharField(max_length=50),
        ),
    ]
