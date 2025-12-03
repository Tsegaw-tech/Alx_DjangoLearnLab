from django.urls import path
from . import views

from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentUpdateView, CommentDeleteView, comment_create_view,
    # other imports...
)

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page at '/'
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog posts CRUD
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),


    path('post/<int:post_pk>/comment/new/', comment_create_view, name='comment-create'),
    path('post/comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
