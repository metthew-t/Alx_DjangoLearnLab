# api/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book
from datetime import datetime


class BookViewTests(APITestCase):
    """
    Test cases for Book API views.
    Tests CRUD operations and custom view functionality.
    """
    
    def setUp(self):
        """Set up test data before each test."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )
        
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.pk])
        self.book_create_url = reverse('book-create')
        self.book_update_url = reverse('book-update', args=[self.book.pk])
        self.book_delete_url = reverse('book-delete', args=[self.book.pk])
        self.book_year_range_url = reverse('book-year-range')
    
    def test_list_books_unauthenticated(self):
        """Test that anyone can list books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_create_book_authenticated(self):
        """Test that authenticated users can create books."""
        self.client.force_authenticate(user=self.user)
        
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_update_book_authenticated(self):
        """Test that authenticated users can update books."""
        self.client.force_authenticate(user=self.user)
        
        data = {
            'title': 'Updated Book',
            'publication_year': 2021,
            'author': self.author.pk
        }
        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
    
    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete books."""
        self.client.force_authenticate(user=self.user)
        
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_book_year_range_view(self):
        """Test the custom BookYearRangeView."""
        # Create another book for testing
        Book.objects.create(
            title='Old Book',
            publication_year=2010,
            author=self.author
        )
        
        # Test valid range
        response = self.client.get(
            self.book_year_range_url,
            {'start_year': '2000', 'end_year': '2020'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_book_year_range_view_missing_params(self):
        """Test BookYearRangeView with missing parameters."""
        response = self.client.get(self.book_year_range_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_book_search(self):
        """Test search functionality."""
        response = self.client.get(self.book_list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_book_filtering(self):
        """Test filtering by publication year."""
        response = self.client.get(
            self.book_list_url,
            {'publication_year': '2020'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_book_ordering(self):
        """Test ordering of books."""
        # Create another book for ordering test
        Book.objects.create(
            title='Another Book',
            publication_year=2019,
            author=self.author
        )
        
        response = self.client.get(self.book_list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))


class AuthorViewTests(APITestCase):
    """Test cases for Author API views."""
    
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Test Author')
        
        # Create books for the author
        Book.objects.create(
            title='Book 1',
            publication_year=2020,
            author=self.author
        )
        Book.objects.create(
            title='Book 2',
            publication_year=2021,
            author=self.author
        )
        
        self.author_list_url = reverse('author-list')
        self.author_detail_url = reverse('author-detail', args=[self.author.pk])
    
    def test_list_authors(self):
        """Test listing authors."""
        response = self.client.get(self.author_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_author_detail_with_books(self):
        """Test retrieving author detail with nested books."""
        response = self.client.get(self.author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Author')
        self.assertEqual(len(response.data['books']), 2)