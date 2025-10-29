# Retrieve the updated book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# Expected Output:
# (1, {'bookshelf.Book': 1})

# Confirm deletion by checking all books
Book.objects.all()
# Expected Output:
# <QuerySet []>
