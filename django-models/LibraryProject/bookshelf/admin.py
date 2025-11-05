from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ("title", "author", "publication_year")

    # Filters displayed in the sidebar
    list_filter = ("publication_year", "author")

    # Search box to find books by title or author
    search_fields = ("title", "author")
