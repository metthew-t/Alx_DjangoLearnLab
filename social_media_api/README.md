# Social Media API

A Django REST Framework-based API for a social media platform, featuring custom user authentication with token-based login.

## Setup Instructions

1. **Clone the repository** (if applicable).
2. **Create a virtual environment** and activate it.
3. **Install dependencies**:
   ```bash
   pip install django djangorestframework Pillow

   ## Posts & Comments API

All endpoints are under `/api/`.

| Method | Endpoint                | Description                          | Auth Required |
|--------|-------------------------|--------------------------------------|---------------|
| GET    | `/posts/`               | List all posts (paginated)           | No            |
| POST   | `/posts/`               | Create a new post                    | Yes           |
| GET    | `/posts/{id}/`          | Retrieve a single post                | No            |
| PUT    | `/posts/{id}/`          | Update a post (full update)           | Yes (author)  |
| PATCH  | `/posts/{id}/`          | Partial update                        | Yes (author)  |
| DELETE | `/posts/{id}/`          | Delete a post                         | Yes (author)  |
| GET    | `/comments/`            | List all comments (optional `?post=`) | No            |
| POST   | `/comments/`            | Create a comment                      | Yes           |
| GET    | `/comments/{id}/`       | Retrieve a comment                     | No            |
| PUT    | `/comments/{id}/`       | Update a comment                       | Yes (author)  |
| DELETE | `/comments/{id}/`       | Delete a comment                       | Yes (author)  |

### Filtering & Searching
- Posts: `?search=<term>` (title + content) , `?author=<user_id>`
- Comments: `?post=<post_id>`

### Pagination
Default page size: 10. Use `?page=<number>` to navigate.

### Example Requests

**Create a post**