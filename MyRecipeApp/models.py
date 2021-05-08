from django.db import models


class MRecipe(models.Model):
    pass
    
class Dish(models.Model):
    rName = models.TextField(default='')
    rNameofDish = models.TextField(default='')
    rMainRecipe = models.TextField(default='')
    rIngredients = models.TextField(default='')
    rProcedures = models.TextField(default='') 
    recipe = models.ForeignKey(MRecipe, default=None, on_delete=models.PROTECT)




