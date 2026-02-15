# Blog Post Management Features

## Overview
This module provides full CRUD (Create, Read, Update, Delete) functionality for blog posts. It uses Django's class-based views and permission mixins to ensure secure and intuitive content management.

## Features

### Post List (`/posts/`)
- Displays all blog posts in reverse chronological order.
- Shows title, author, publication date, and a snippet of content.
- Authenticated users see a "Create New Post" link.
- Authors see Edit/Delete links next to their own posts.

### Post Detail (`/posts/<id>/`)
- Shows full post content with author and date.
- Authors see Edit and Delete buttons.

### Create Post (`/posts/new/`)
- Accessible only to logged-in users.
- Form includes title and content fields.
- Author is automatically set to the current user.

### Update Post (`/posts/<id>/edit/`)
- Accessible only to the post's author.
- Pre-filled form for editing.
- Saves changes and redirects to list.

### Delete Post (`/posts/<id>/delete/`)
- Accessible only to the post's author.
- Confirmation page before deletion.
- After deletion, redirects to list.

## Permissions
- **Anonymous users**: Can view list and detail only.
- **Authenticated users**: Can create posts, and edit/delete only their own.
- Enforcement via `LoginRequiredMixin` and `UserPassesTestMixin`.

## Templates
All templates are located in `blog/templates/blog/`:
- `post_list.html` – displays all posts.
- `post_detail.html` – shows a single post.
- `post_form.html` – used for both create and edit.
- `post_confirm_delete.html` – delete confirmation.

## URLs
Defined in `blog/urls.py`:
- `posts/` – list
- `posts/new/` – create
- `posts/<int:pk>/` – detail
- `posts/<int:pk>/edit/` – update
- `posts/<int:pk>/delete/` – delete

## Testing Instructions
1. Run server: `python manage.py runserver`
2. As anonymous: navigate to `/posts/` – view only.
3. Register/login: create a post.
4. Logout, then log in as a different user: attempt to edit/delete the first user's post – you should receive a 403 error.
5. Verify that all links and redirects work as expected.