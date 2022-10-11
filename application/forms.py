from django.contrib.auth.forms import UserCreationForm
from .models import User, Recipe
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'password1', 'password2']


class EditUserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'image']


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {'ingredients': forms.Textarea(), 'recipe': forms.Textarea(),
                   'user': forms.HiddenInput()}
