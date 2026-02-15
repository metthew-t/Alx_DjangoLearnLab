# Tagging and Search Features

## Tagging
- **Adding tags**: When creating or editing a post, enter tags as comma-separated values (e.g., `python, django, tutorial`).
- **Viewing tags**: Each post's detail page shows its tags as clickable links.
- **Filtering by tag**: Clicking a tag displays all posts containing that tag.

## Search
- The search bar is available on the home page and the posts list page.
- Enter keywords to search across post titles, content, and tag names.
- Results are displayed on a dedicated search results page.

## Implementation Details
- Tagging uses `django-taggit` for easy management.
- Search uses Django's `Q` objects to combine filters on title, content, and tags.

## URLs
- `/tags/<tag_name>/` – list posts by tag.
- `/search/` – search endpoint (GET parameter `q`).

## Testing
1. Create a post with tags.
2. Verify tags appear on detail page.
3. Click a tag to see filtered list.
4. Use search bar with various keywords to confirm results.