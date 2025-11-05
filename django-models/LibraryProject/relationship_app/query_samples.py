from relationship_app.models import Author, Book, Library, Librarian
from relationship_app.query_samples import *

# Create data
a1 = Author.objects.create(name="Jane Doe")
b1 = Book.objects.create(title="Python Basics", author=a1)
b2 = Book.objects.create(title="Advanced Django", author=a1)
lib = Library.objects.create(name="Central Library")
lib.books.set([b1, b2])
Librarian.objects.create(name="John Smith", library=lib)

# Test queries
print(query_books_by_author("Jane Doe"))
print(list_books_in_library("Central Library"))
print(get_librarian_for_library("Central Library"))
