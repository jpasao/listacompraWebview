from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ..forms.meal_forms import *
from ..models import Meal, Ingredient, Mealingredient


@login_required
def meal_list(request):
    form = FilterMealForm(request.GET)
    meals = Meal.objects.all()
    ingredients = Ingredient.objects.defer().order_by('name')
    current_meals = meals.filter(ischecked__exact=0)
    possible_meals = meals.filter(ischecked__exact=1).order_by('name')
    lunches = current_meals.filter(islunch__exact=1).order_by('name')
    dinners = current_meals.filter(islunch__exact=0).order_by('name')

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            lunches = lunches.filter(name__icontains=search)
            dinners = dinners.filter(name__icontains=search)
            possible_meals = possible_meals.filter(name__icontains=search)

    return render(
        request,
        'meal/meal_list.html',
        {
            'lunches': lunches,
            'dinners': dinners,
            'possible_meals': possible_meals,
            'ingredients': ingredients,
            'form': form
        })

@login_required
def meal_new(request):
    form = MealForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            meal = form.save()
            meal.save()
            return redirect('meal_list')

    return render(request, 'meal/meal_edit.html', {'form': form})

@login_required
def meal_edit(request, pk):
    item = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('meal_list')
    else:
        form = MealForm(instance=item)

    return render(request, 'meal/meal_edit.html', {'form': form})

@login_required
def meal_choose(request, pk):
    return meal_set_meal(request, pk, True)

@login_required
def meal_choose_dinner(request, pk):
    return meal_set_meal(request, pk, False)

@login_required
def meal_set_meal(request, pk, is_lunch):
    item = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = ChooseMealForm(request.POST, instance=item)
        if form.is_valid():
            item.ischecked = 0
            item.islunch = 1 if is_lunch else 0
            item = form.save()
    else:
        form = ChooseMealForm(instance=item)

    return redirect('meal_list')

@login_required
def meal_check(request, pk):
    item = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = CheckMealForm(request.POST, instance=item)
        if form.is_valid():
            item.ischecked = 1
            item = form.save()
    else: 
        form = CheckMealForm(instance=item)

    return redirect('meal_list')

@login_required
def meal_delete(_, pk):
    item = get_object_or_404(Meal, pk=pk)
    item.delete()

    return redirect('meal_list')

@login_required
def meal_get_ingredients(request, pk):
    meal_ingredients = Mealingredient.objects.filter(mealid__exact=pk)
    ingredients = {}
    items = []
    for item in meal_ingredients:
        items.append(item.ingredientid_id)
    ingredients['data'] = items

    return JsonResponse(ingredients)

@login_required
def meal_set_ingredients(request, pk):
    if request.method == 'POST':
        form = MealIngredientsForm(request.POST)

        if form.is_valid():
            items_to_delete = Mealingredient.objects.filter(mealid__exact=pk)
            if items_to_delete.count() > 0:
                items_to_delete.delete()

            data = form.cleaned_data['ingredients']['data']
            deserialized = set(data)
            for item in deserialized:
                meal = get_object_or_404(Meal, pk=pk)
                ingredient = get_object_or_404(Ingredient, pk=item)
                Mealingredient.objects.create(mealid=meal, ingredientid=ingredient)
    else:
        form = MealIngredientsForm(request.POST)

    return redirect('meal_list')
