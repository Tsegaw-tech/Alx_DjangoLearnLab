from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from .models import Book, Library
from django.views import View
from django.views.generic import DetailView


=======
from django.views.generic import DetailView
from .models import Book
from .models import Library
>>>>>>> 2cc6c9f (Django Views and URL Configuration3)


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})


class LibraryDetailView(DetailView):
    """Display a single library and all its books."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


