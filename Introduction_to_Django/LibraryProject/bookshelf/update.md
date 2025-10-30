# Retrieve the specific book
book = Book.objects.get(title="1984")

# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated record
print(book.title, book.author, book.publication_year)
# Expected Output:
# Nineteen Eighty-Four George Orwell 1949
