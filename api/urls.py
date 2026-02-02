"""
URL configuration for API app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    path('test-serializers/', views.TestSerializerView.as_view(), name='test-serializers'),
]