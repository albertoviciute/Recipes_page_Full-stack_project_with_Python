from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.utils.decorators import method_decorator

from .models import Recipe, Category
from django.db.models import Q
from .forms import SignUpForm, EditUserAccountForm, CreateRecipeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    recipes_quantity = Recipe.objects.count()
    context = {
        'recipes_quantity': recipes_quantity,
    }
    return render(request, 'home.html', context=context)


def show_recipes(request):
    category = Category.objects.all()
    paginator = Paginator(Recipe.objects.all(), 9)
    page_number = request.GET.get('page')
    paged_recipes = paginator.get_page(page_number)
    context = {
        'recipes': paged_recipes,
        'category': category,
    }
    return render(request, 'show_recipes.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Recipe.objects.filter(Q(title__icontains=query) | Q(ingredients__icontains=query))
    return render(request, 'search.html', {'recipes': search_results, 'query': query})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


def show_recipe(request, id):
    single_recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'show_recipe.html', {'recipe': single_recipe})


@login_required()
def show_user_recipes(request, page=1):
    recipes_per_page = 9
    recipes = Recipe.objects.filter(user=request.user.id) \
        .values('title', 'image', 'id')
    paginator = Paginator(recipes, recipes_per_page)
    paginated_recipes = paginator.get_page(page)
    context = {
        'recipes': paginated_recipes
    }
    return render(request, 'show_user_recipes.html', context=context)


@method_decorator(login_required, name='dispatch')
class CreateRecipeView(LoginRequiredMixin, CreateView):
    form_c = CreateRecipeForm
    context = {}
    template_name = 'create_recipes.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        self.context['form'] = self.form_c(initial={'user': user})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_c(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_user_recipes', page=1)
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class EditRecipe(UpdateView):
    form_c = CreateRecipeForm
    context = {}
    template_name = 'create_recipes.html'

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        recipes = get_object_or_404(Recipe, pk=id)
        form = self.form_c(instance=recipes)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        recipes = get_object_or_404(Recipe, pk=id)
        form = self.form_class(instance=recipes, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_user_recipes', page=1)
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteRecipe(DeleteView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        recipes = get_object_or_404(Recipe, pk=id)
        recipes.delete()
        return redirect('show_user_recipes', page=1)


def user_account(request):
    if request.method == 'POST':
        form = EditUserAccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_account')
    else:
        form = EditUserAccountForm(
            initial={
                'email': request.user.email,
                'image': request.user.image
            }
        )
    return render(request, 'user_account.html', context={'form': form})


def appetizers(request):
    search_results = Recipe.objects.filter(category__category='Appetizers').values()
    return render(request, 'appetizers.html', {'recipes': search_results})


def desserts(request):
    search_results = Recipe.objects.filter(category__category='Desserts').values()
    return render(request, 'desserts.html', {'recipes': search_results})


def soups(request):
    search_results = Recipe.objects.filter(category__category='Soups').values()
    return render(request, 'soups.html', {'recipes': search_results})


def meat(request):
    search_results = Recipe.objects.filter(category__category='Meat').values()
    return render(request, 'meat.html', {'recipes': search_results})


def vegetarian(request):
    search_results = Recipe.objects.filter(category__category='Vegetarian').values()
    return render(request, 'vegetarian.html', {'recipes': search_results})


def sauces(request):
    search_results = Recipe.objects.filter(category__category='Sauces').values()
    return render(request, 'sauces.html', {'recipes': search_results})


def side_dishes(request):
    search_results = Recipe.objects.filter(category__category='Side dishes').values()
    return render(request, 'side_dishes.html', {'recipes': search_results})
