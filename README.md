# Advanced API Project

## Project Overview
This project demonstrates advanced API development using Django REST Framework with custom serializers, nested relationships, and data validation.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Alx_DjangoLearnLab
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
```bash
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

## API Endpoints

- `GET /api/authors/` - List all authors with nested books
- `POST /api/authors/` - Create new author
- `GET /api/books/` - List all books
- `POST /api/books/` - Create new book with validation
- `GET /api/test-serializers/` - Test serializers

## Models

### Author
- `name` (CharField): Author's full name

### Book
- `title` (CharField): Book title
- `publication_year` (IntegerField): Year of publication
- `author` (ForeignKey): Link to Author model

## Serializers

### BookSerializer
- Includes custom validation for publication year
- Prevents future publication years
- Object-level validation for unique books per author

### AuthorSerializer
- Nested serialization of related books
- Includes book count field
- Name validation for letters and spaces only

## Testing
Test using:
1. Django Admin: http://localhost:8000/admin/
2. Django Shell: `python manage.py shell`
3. API endpoints: http://localhost:8000/api/

## Validation Rules
1. Publication year cannot be in the future
2. Publication year must be ≥ 1000
3. Book title must be unique per author
4. Author name must contain only letters and spaces