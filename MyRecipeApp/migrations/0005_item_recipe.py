# Generated by Django 3.1.6 on 2021-05-02 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipeApp', '0004_remove_item_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='MyRecipeApp.mrecipe'),
        ),
    ]
