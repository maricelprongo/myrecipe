# Generated by Django 3.1.6 on 2021-06-03 23:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipeApp', '0011_auto_20210510_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cDate', models.DateField(blank=True, default=datetime.date(1111, 11, 11), help_text='Today Date.', null=True)),
                ('cName', models.TextField(default='')),
                ('cComments', models.TextField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crName', models.TextField(default='')),
                ('crGender', models.TextField(default='')),
                ('crEAddress', models.EmailField(default='', max_length=254)),
                ('crContactNumber', models.CharField(default='', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rQuantity', models.TextField(default='')),
                ('rUnit', models.TextField(default='')),
                ('rIngredients', models.TextField(default='')),
                ('rProcedures', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.TextField(default='')),
                ('uEAddress', models.EmailField(default='', max_length=254)),
                ('CommentId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='MyRecipeApp.comments')),
            ],
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='rIngredients',
            new_name='dCategory',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='rMainRecipe',
            new_name='dDifficulty',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='rName',
            new_name='dMainIngredient',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='rNameofDish',
            new_name='dNameofDish',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='rProcedures',
            new_name='dServings',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='recipe',
        ),
        migrations.AddField(
            model_name='dish',
            name='dDate',
            field=models.DateField(blank=True, default=datetime.date(1111, 11, 11), help_text='Today Date.', null=True),
        ),
        migrations.DeleteModel(
            name='MRecipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='DishId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='MyRecipeApp.dish'),
        ),
        migrations.AddField(
            model_name='comments',
            name='DishId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='MyRecipeApp.dish'),
        ),
        migrations.AddField(
            model_name='dish',
            name='CreatorId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='MyRecipeApp.creator'),
        ),
    ]
