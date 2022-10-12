from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='photos')
    recipe = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    time = models.CharField(max_length=5)
    servings = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    topic = models.CharField(max_length=500)
    feedback = models.TextField(null=True)