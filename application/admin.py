from django.contrib import admin
from .models import User, Category, Recipe, Feedback

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Feedback)
