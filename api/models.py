"""
Models for Author and Book.
"""

from django.db import models

class Author(models.Model):
    """
    Author model representing an author in the system.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Author Name",
        help_text="Enter the full name of the author"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Book(models.Model):
    """
    Book model representing a book in the system.
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Book Title",
        help_text="Enter the title of the book"
    )
    
    publication_year = models.IntegerField(
        verbose_name="Publication Year",
        help_text="Enter the year the book was published"
    )
    
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name="Book Author",
        help_text="Select the author of this book"
    )
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_book_per_author'
            )
        ]