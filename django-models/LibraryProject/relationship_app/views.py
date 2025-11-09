from django.shortcuts import render, get_object_or_404
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})
