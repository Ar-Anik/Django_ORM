# Generated by Django 4.0.2 on 2022-02-22 12:30

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bangladeshi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('Nid', models.TextField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.TextField(max_length=100)),
                ('std_id', models.IntegerField()),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one.bangladeshi')),
            ],
        ),
    ]