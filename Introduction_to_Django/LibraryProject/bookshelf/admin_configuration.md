"# Django Admin Interface Configuration" 
 
"## 1. Book Model Registration" 
"Registered the Book model in \`bookshelf/admin.py\`:" 
"\`\`\`python" 
"from django.contrib import admin" 
"from .models import Book" 
 
"@admin.register(Book)" 
"class BookAdmin(admin.ModelAdmin):" 
"    list_display = ('title', 'author', 'publication_year')" 
"    list_filter = ('publication_year', 'author')" 
"    search_fields = ('title', 'author')" 
"\`\`\`" 
 
"## 2. Admin Features Implemented" 
 
"### List Display" 
"- Shows title, author, and publication year in a table format" 
"- Makes it easy to scan through book entries" 
 
"### List Filters" 
"- Filter books by publication year" 
"- Filter books by author" 
"- Enables quick filtering of large datasets" 
 
"### Search Fields" 
"- Search books by title" 
"- Search books by author" 
"- Allows quick finding of specific books" 
 
"## 3. Superuser Creation" 
"Created superuser using:" 
"\`\`\`bash" 
"python manage.py createsuperuser" 
"\`\`\`" 
"Credentials:" 
"- Username: admin" 
"- Password: admin123" 
 
"## 4. Admin URL" 
"Access the admin interface at: http://127.0.0.1:8000/admin/" 
 
"## 5. Sample Data Added via Admin" 
"1. **To Kill a Mockingbird** by Harper Lee (1960)" 
"2. **The Great Gatsby** by F. Scott Fitzgerald (1925)" 
"3. **Pride and Prejudice** by Jane Austen (1813)" 
