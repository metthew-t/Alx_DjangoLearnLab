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


## Follow System & Feed

### Follow/Unfollow Endpoints
All endpoints require authentication (Token).

- **Follow a user**  
  `POST /api/accounts/follow/<user_id>/`  
  Adds the target user to your following list.  
  *Response:* `{"message": "You are now following <username>."}`

- **Unfollow a user**  
  `POST /api/accounts/unfollow/<user_id>/`  
  Removes the target user from your following list.  
  *Response:* `{"message": "You have unfollowed <username>."}`

### Feed Endpoint
- **Get your feed**  
  `GET /api/feed/`  
  Returns a paginated list of posts from users you follow, ordered by most recent.  
  Requires authentication.  
  *Response:* List of posts (same format as `/posts/`).

### Example
```bash
# Follow user with ID 2
curl -X POST http://127.0.0.1:8000/api/accounts/follow/2/ \
  -H "Authorization: Token YOUR_TOKEN"

# Get feed
curl http://127.0.0.1:8000/api/feed/ \
  -H "Authorization: Token YOUR_TOKEN"