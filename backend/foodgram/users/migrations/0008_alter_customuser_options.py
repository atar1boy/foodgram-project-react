# Generated by Django 4.2.2 on 2023-07-01 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
