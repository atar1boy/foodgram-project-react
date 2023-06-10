# Generated by Django 4.2.2 on 2023-06-10 15:26

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=96, unique=True)),
                ('measurement_unit', models.CharField(max_length=96)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=96, unique=True)),
                ('slug', models.SlugField(max_length=96, unique=True)),
                ('colour', colorfield.fields.ColorField(default='#30d5c8', image_field=None, max_length=18, samples=None, unique=True, verbose_name='Цвет в HEX')),
            ],
        ),
    ]
