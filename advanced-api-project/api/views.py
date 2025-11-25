from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
Book CRUD API using Django REST Framework Generic Views.
These views handle the logic for listing, creating, retrieving,
updating, and deleting books with minimal code.
"""


# GET /books/ — List all Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public (Read-only)


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
