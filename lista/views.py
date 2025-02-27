from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Authors

@login_required
def author_list(request):
    authors = Authors.objects.order_by('authorid')
    return render(request, 'lista/author_list.html', {'authors': authors})
