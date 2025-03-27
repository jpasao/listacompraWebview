from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..forms.other_forms import *
from ..models import Otherparent, Otherchild

@login_required
def other_list(request):
    form = FilterOtherForm(request.GET)
    parents = Otherparent.objects.all().order_by('name')
    children = Otherchild.objects.all().order_by('name')
    checked_children = children.filter(ischecked__exact=1)
    unchecked_children = children.filter(ischecked__exact=0)

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            checked_children = checked_children.filter(name__icontains=search)
            unchecked_children = unchecked_children.filter(name__icontains=search)
            parents_found = list(children
                                 .filter(name__icontains=search)
                                 .values_list('parentid', flat=True))
            parents = [d for d in parents if d.id in parents_found]
    return render(
        request,
        'other/other_list.html',
        {
            'parents': parents,
            'checked_children': checked_children,
            'unchecked_children': unchecked_children,
            'form': form
        })

@login_required
def other_new(request):
    form = OtherForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            other = form.save()
            other.save()
            return redirect('other_list')

    return render(request, 'other/other_edit.html', {'form': form})

@login_required
def other_edit(request, pk):
    item = get_object_or_404(Otherchild, pk=pk)
    if request.method == 'POST':
        form = OtherForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('other_list')
    else:
        form = OtherForm(instance=item)

    return render(request, 'other/other_edit.html', {'form': form})

@login_required
def other_check(request, pk):
    return other_change(request, pk, True)

@login_required
def other_uncheck(request, pk):
    return other_change(request, pk, False)

def other_change(request, pk, check):
    item = get_object_or_404(Otherchild, pk=pk)
    if request.method == 'POST':
        form = CheckOtherForm(request.POST, instance=item)
        if form.is_valid():
            item.ischecked = 1 if check else 0
            item = form.save()
    else: 
        form = CheckOtherForm(instance=item)

    return redirect('other_list')

@login_required
def other_delete(_, pk):
    item = get_object_or_404(Otherchild, pk=pk)
    item.delete()

    return redirect('other_list')

########## Other parent views ##########

@login_required
def other_parent_list(request):
    form = FilterOtherParentForm(request.GET)
    parents = Otherparent.objects.all().order_by('name')

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            parents = parents.filter(name__icontains=search)

    return render(
        request,
        'other/other_parent_list.html',
        {
            'parents': parents,
            'form': form
        })

@login_required
def other_parent_new(request):
    form = OtherParentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            other_parent = form.save()
            other_parent.save()
            return redirect('other_parent_list')

    return render(request, 'other/other_parent_edit.html', {'form': form})

@login_required
def other_parent_edit(request, pk):
    item = get_object_or_404(Otherparent, pk=pk)
    if request.method == 'POST':
        form = OtherParentForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('other_parent_list')
    else:
        form = OtherParentForm(instance=item)

    return render(request, 'other/other_parent_edit.html', {'form': form})

@login_required
def other_parent_delete(_, pk):
    item = get_object_or_404(Otherparent, pk=pk)
    item.delete()

    return redirect('other_parent_list')

