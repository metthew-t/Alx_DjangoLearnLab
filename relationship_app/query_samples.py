from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()


# List all books in a library
def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian