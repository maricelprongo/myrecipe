# Generated by Django 3.1.6 on 2021-05-10 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipeApp', '0010_merge_20210510_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='text',
        ),
        migrations.RemoveField(
            model_name='mrecipe',
            name='rDishType',
        ),
        migrations.RemoveField(
            model_name='mrecipe',
            name='rUserName',
        ),
    ]
