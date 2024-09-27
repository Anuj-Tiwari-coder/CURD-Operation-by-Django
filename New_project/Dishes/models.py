from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    recipe_view_count= models.IntegerField(default= 1)


