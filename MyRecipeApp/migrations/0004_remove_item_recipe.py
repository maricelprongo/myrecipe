# Generated by Django 3.1.6 on 2021-05-02 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipeApp', '0003_auto_20210502_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='recipe',
        ),
    ]
