# Retrieve all book records
books = Book.objects.all()

# Display book details
for b in books:
    print(b.title, b.author, b.publication_year)

# Expected Output:
# 1984 George Orwell 1949
