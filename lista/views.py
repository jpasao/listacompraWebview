from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Author
from .models import Ingredient

@login_required
def author_list(request):
    authors = Author.objects.order_by('authorid')
    return render(request, 'author/author_list.html', {'authors': authors})

@login_required
def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            author.save()
            return redirect('author_list')
    else:
        form = AuthorForm()

    return render(request, 'author/author_edit.html', {'form': form})

@login_required
def ingredient_list(request):
    form = FilterIngredientForm(request.GET or None)
    ingredients = Ingredient.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            ingredients = ingredients.filter(name__icontains=search)
    return render(request, 'ingredient/ingredient_list.html', {'ingredients': ingredients, 'form': form})

@login_required
def ingredient_new(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)

        if form.is_valid():
            ingredient = form.save()
            ingredient.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()

    return render(request, 'ingredient/ingredient_edit.html', {'form': form})