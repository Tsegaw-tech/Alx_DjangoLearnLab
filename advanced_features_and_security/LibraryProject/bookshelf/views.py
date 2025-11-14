from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Book
from .forms import ExampleForm


# -----------------------------
# Forms for secure input handling
# -----------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search Books")

# -----------------------------
# Views
# -----------------------------

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # ORM handles parameterization safely
            books = books.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})



# View to display and handle ExampleForm
@permission_required('bookshelf.can_create', raise_exception=True)
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            data = form.cleaned_data
            # For demonstration, let's say ExampleForm has 'name' and 'email'
            print(f"Received name: {data['name']}, email: {data['email']}")
            # You could save data to a model here if needed
            return redirect('relationship_app:list_books')  # redirect after success
    else:
        form = ExampleForm()  # empty form for GET request

    return render(request, 'bookshelf/form_example.html', {'form': form})
