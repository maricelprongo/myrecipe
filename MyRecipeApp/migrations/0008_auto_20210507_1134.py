# Generated by Django 3.1.6 on 2021-05-07 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipeApp', '0007_auto_20210507_1124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Dish',
        ),
    ]
