"""
Admin configuration for Author and Book models.
"""

from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']
    search_fields = ['name']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_filter = ['author', 'publication_year']
    search_fields = ['title', 'author__name']
    raw_id_fields = ['author']