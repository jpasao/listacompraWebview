from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from ..forms.ingredient_forms import *
from ..models import Ingredient

@login_required
def ingredient_list(request):
    form = FilterIngredientForm(request.GET or None)
    check_form = CheckIngredientForm(request.POST)
    ingredients = Ingredient.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            ingredients = (ingredients
                           .filter(Q(name__icontains=search) | Q(comment__icontains=search))
                           .order_by('name'))

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
        form = IngredientForm(request.POST)

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

@login_required
def ingredient_increase(request, pk):
    return ingredient_modify_quantity(request, pk, True)

@login_required
def ingredient_decrease(request, pk):
    return ingredient_modify_quantity(request, pk, False)

def ingredient_modify_quantity(request, pk, increase):
    item = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = QuantityIngredientForm(request.POST, instance=item)
        if form.is_valid():
            item.isproduct = '\x01'
            increment = 1 if increase else - 1
            item.quantity += increment 
            if item.quantity == 0: item.quantity = 1
            item = form.save()
    else: 
        form = QuantityIngredientForm(instance=item)

    return redirect('ingredient_list')

@login_required
def ingredient_delete(request, pk):
    item = get_object_or_404(Ingredient, pk=pk)
    item.delete()

    return redirect('ingredient_list')
