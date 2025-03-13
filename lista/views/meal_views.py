from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from ..forms.meal_forms import *
from ..models import Meal

@login_required
def meal_list(request):
    form = FilterMealForm(request.GET)
    meals = Meal.objects.all()
    current_meals = meals.filter(ischecked__exact=0)
    possible_meals = meals.filter(ischecked__exact=1)
    lunches = current_meals.filter(islunch__exact=1).order_by('name')
    dinners = current_meals.filter(islunch__exact=0).order_by('name')

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            lunches = lunches.filter(name__icontains=search)
            dinners = dinners.filter(name__icontains=search)

    return render(
        request,
        'meal/meal_list.html',
        {
            'lunches': lunches,
            'dinners': dinners,
            'possible_meals': possible_meals,
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