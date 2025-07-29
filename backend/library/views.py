# events/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from library.models import Library

def index(request):
    library = Library.objects.all().order_by('-created')
    return render(request, 'library/index.html', {"library": library})

def library_detail(request, pk):
    item = get_object_or_404(Library, pk=pk)
    return render(request, 'library/detail.html', {'item': item})