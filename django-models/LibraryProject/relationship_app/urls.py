from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
]
