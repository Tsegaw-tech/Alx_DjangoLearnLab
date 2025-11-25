from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters_rest_framework


"""
Book CRUD API using Django REST Framework Generic Views.
These views handle the logic for listing, creating, retrieving,
updating, and deleting books with minimal code.
"""


# GET /books/ — List all Books
class BookListView(generics.ListAPIView):
    """
    BookListView supports:
    - Filtering (title, author, publication_year)
    - Searching (title, author__name)
    - Ordering (title, publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering: /books/?title=ABC&publication_year=2020
    filterset_fields = ['title', 'publication_year', 'author']

    # Searching: /books/?search=chinua
    search_fields = ['title', 'author__name']

    # Ordering: /books/?ordering=title  OR  /books/?ordering=-publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering



# GET /books/<id>/ — Retrieve a single Book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public (Read-only)


# POST /books/ — Create a new Book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can create

    def perform_create(self, serializer):
        """
        Custom behavior during creation.
        You can add logics such as:
        - Automatically add metadata
        - Validate user roles
        - Custom response handling
        """
        serializer.save()


# PUT/PATCH /books/<id>/ — Update an existing Book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can update

    def perform_update(self, serializer):
        """
        Hook to customize update behavior.
        Here you can implement:
        - Role checks
        - Logging
        """
        serializer.save()


# DELETE /books/<id>/ — Delete a Book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can delete
