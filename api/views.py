"""
Views for testing serializers.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    View to list all books and create new books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    """
    View to list all authors and create new authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TestSerializerView(APIView):
    """
    View to test serializers manually.
    """
    def get(self, request):
        # Create test data if none exists
        if not Author.objects.exists():
            author = Author.objects.create(name="Test Author")
            Book.objects.create(
                title="Test Book",
                publication_year=2020,
                author=author
            )
        
        author = Author.objects.first()
        author_data = AuthorSerializer(author).data
        
        return Response({
            'author_with_books': author_data,
            'message': 'Test data created. Check Django admin or shell for more testing.'
        })