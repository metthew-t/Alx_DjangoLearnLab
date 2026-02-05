# api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListView(generics.ListAPIView):
    """
    ListView for retrieving all books with filtering, searching, and ordering capabilities.
    Uses DRF's generic ListAPIView for efficient list operations.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view books
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView for retrieving a single book by ID.
    Uses DRF's generic RetrieveAPIView for single object retrieval.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view book details
    lookup_field = 'pk'


class BookCreateView(generics.CreateAPIView):
    """
    CreateView for adding a new book.
    Uses DRF's generic CreateAPIView for object creation.
    Custom validation is handled by the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books
    
    def perform_create(self, serializer):
        """
        Override to add custom behavior during creation.
        Could be used to log who created the book or add additional validation.
        """
        serializer.save()
        print(f"Book created: {serializer.instance.title}")


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView for modifying an existing book.
    Uses DRF's generic UpdateAPIView for object updates.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        """
        Override to add custom behavior during update.
        """
        serializer.save()
        print(f"Book updated: {serializer.instance.title}")


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView for removing a book.
    Uses DRF's generic DestroyAPIView for object deletion.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete books
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        """
        Override to add custom behavior during deletion.
        """
        print(f"Deleting book: {instance.title}")
        instance.delete()


# Custom View for Specific Use Case
class BookYearRangeView(APIView):
    """
    Custom View example: Get books published within a specific year range.
    Demonstrates custom view implementation beyond generic views.
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        """
        Handle GET requests to filter books by year range.
        Expected query parameters: start_year, end_year
        """
        start_year = request.query_params.get('start_year')
        end_year = request.query_params.get('end_year')
        
        if not start_year or not end_year:
            return Response(
                {'error': 'Both start_year and end_year query parameters are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            start_year = int(start_year)
            end_year = int(end_year)
            
            if start_year > end_year:
                return Response(
                    {'error': 'start_year cannot be greater than end_year'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            books = Book.objects.filter(
                publication_year__gte=start_year,
                publication_year__lte=end_year
            )
            
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
            
        except ValueError:
            return Response(
                {'error': 'Year parameters must be valid integers'},
                status=status.HTTP_400_BAD_REQUEST
            )


# Author Views (for completeness)
class AuthorListView(generics.ListAPIView):
    """
    ListView for retrieving all authors with their books.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['name']


class AuthorDetailView(generics.RetrieveAPIView):
    """
    DetailView for retrieving a single author by ID with their books.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'