"""
Serializers for Author and Book models.
"""

from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model with custom validation.
    """
    author_name = serializers.CharField(
        source='author.name',
        read_only=True,
        help_text="Name of the book's author"
    )
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'author_name']
        extra_kwargs = {
            'title': {'required': True},
            'publication_year': {'required': True},
            'author': {'required': True}
        }
    
    def validate_publication_year(self, value):
        """
        Validate that publication year is not in the future.
        """
        current_year = timezone.now().year
        
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. "
                f"Current year is {current_year}."
            )
        
        if value < 1000:
            raise serializers.ValidationError(
                "Publication year should be 1000 or later."
            )
        
        return value
    
    def validate(self, data):
        """
        Object-level validation to prevent duplicate books per author.
        """
        instance = self.instance
        title = data.get('title', getattr(instance, 'title', None))
        author = data.get('author', getattr(instance, 'author', None))
        
        if instance:
            exists = Book.objects.filter(
                title=title,
                author=author
            ).exclude(id=instance.id).exists()
        else:
            exists = Book.objects.filter(title=title, author=author).exists()
        
        if exists:
            raise serializers.ValidationError({
                'title': f"A book with this title already exists for {author.name}."
            })
        
        return data


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model with nested books.
    """
    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField(
        help_text="Total number of books by this author"
    )
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books', 'book_count']
        extra_kwargs = {
            'name': {
                'required': True,
                'min_length': 2,
                'max_length': 100
            }
        }
    
    def get_book_count(self, obj):
        """
        Return the count of books for this author.
        """
        return obj.books.count()
    
    def validate_name(self, value):
        """
        Validate author name contains only letters and spaces.
        """
        value = value.strip()
        
        if not all(c.isalpha() or c.isspace() for c in value):
            raise serializers.ValidationError(
                "Author name should contain only letters and spaces."
            )
        
        return value