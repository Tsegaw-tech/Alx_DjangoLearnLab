
from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Authentication URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]


