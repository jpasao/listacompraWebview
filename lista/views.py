from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    check_form = CheckIngredientForm(request.POST)
    ingredients = Ingredient.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            ingredients = ingredients.filter(Q(name__icontains=search) | Q(comment__icontains=search))

    return render(
        request, 
        'ingredient/ingredient_list.html', 
        {
            'ingredients': ingredients, 
            'form': form, 
            'checkform': check_form
        })

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

@login_required
def ingredient_edit(request, pk):
    item = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=item)
        if form.is_valid():
            item.isproduct = '\x01'
            item = form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=item)

    return render(request, 'ingredient/ingredient_edit.html', {'form': form})

@login_required
def ingredient_check(request, pk):
    item = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = CheckIngredientForm(request.POST, instance=item)
        if form.is_valid():
            item.isproduct = '\x01'
            item.ischecked = '0' if item.ischecked == '0' else '1'
            item = form.save()
    else: 
        form = CheckIngredientForm(instance=item)

    return redirect('ingredient_list')

