# API Documentation - Custom Views and Generic Views

## Overview
This project implements custom views and generic views in Django REST Framework for handling CRUD operations on Book and Author models.

## Views Implemented

### Book Views (Generic Views)

1. **BookListView** (`GET /api/books/`)
   - Purpose: Retrieve all books
   - Permission: Anyone (AllowAny)
   - Features:
     - Filtering by `publication_year` and `author`
     - Search by `title` and `author__name`
     - Ordering by `title` or `publication_year`
     - Default ordering: `title` ascending

2. **BookDetailView** (`GET /api/books/<int:pk>/`)
   - Purpose: Retrieve single book by ID
   - Permission: Anyone (AllowAny)
   - Features: Returns complete book details

3. **BookCreateView** (`POST /api/books/create/`)
   - Purpose: Create new book
   - Permission: Authenticated users only
   - Customization: Overrides `perform_create()` for logging

4. **BookUpdateView** (`PUT/PATCH /api/books/<int:pk>/update/`)
   - Purpose: Update existing book
   - Permission: Authenticated users only
   - Customization: Overrides `perform_update()` for logging

5. **BookDeleteView** (`DELETE /api/books/<int:pk>/delete/`)
   - Purpose: Delete book
   - Permission: Authenticated users only
   - Customization: Overrides `perform_destroy()` for logging

### Custom Views

1. **BookYearRangeView** (`GET /api/books/year-range/`)
   - Purpose: Custom view to filter books by year range
   - Query Parameters:
     - `start_year`: Starting year (required)
     - `end_year`: Ending year (required)
   - Returns: Books published between start_year and end_year
   - Error Handling: Validates parameters and returns appropriate error messages

### Author Views

1. **AuthorListView** (`GET /api/authors/`)
2. **AuthorDetailView** (`GET /api/authors/<int:pk>/`)

## URL Patterns

## Permission Configuration

- **Read Operations**: AllowAny permission (anyone can view)
- **Write Operations**: IsAuthenticated permission (only logged-in users can create/update/delete)

## Testing

Run tests with:
```bash
python manage.py test api.tests