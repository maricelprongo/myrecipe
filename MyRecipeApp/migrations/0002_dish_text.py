# Generated by Django 3.1.6 on 2021-04-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
