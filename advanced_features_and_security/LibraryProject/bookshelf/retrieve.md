# retrieve.md

from bookshelf.models import Book

# Retrieve the book you just created
book = Book.objects.get(title="1984")

# Display book details
print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949
