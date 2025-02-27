from django.shortcuts import render
from .models import Authors

def author_list(request):
    authors = Authors.objects.order_by('authorid')
    return render(request, 'lista/author_list.html', {'authors': authors})
