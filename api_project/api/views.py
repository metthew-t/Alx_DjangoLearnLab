from rest_framework import generics, viewsets, permissions 
from .models import Book 
from .serializers import BookSerializer 
 
# Custom permission example 
class IsAdminOrReadOnly(permissions.BasePermission): 
    def has_permission(self, request, view): 
        # Allow GET, HEAD, OPTIONS requests 
        if request.method in permissions.SAFE_METHODS: 
            return True 
        # Only allow admin users for POST, PUT, DELETE 
        return request.user and request.user.is_staff 
 
class BookList(generics.ListAPIView): 
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
 
class BookViewSet(viewsets.ModelViewSet): 
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAuthenticated]  # Or use [IsAdminOrReadOnly] 
