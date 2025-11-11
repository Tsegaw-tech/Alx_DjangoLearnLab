from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# -------------------------------
# Function-based view
# -------------------------------
def list_books(request):
    """List all books and their authors."""
    books = Book.objects.select_related('author').all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# -------------------------------
# Class-based view
# -------------------------------
class LibraryDetailView(DetailView):
    """Display a single library and all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
