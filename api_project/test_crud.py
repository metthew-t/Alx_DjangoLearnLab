import requests 
import json 
 
BASE_URL = "http://127.0.0.1:8000/api/books_all/" 
 
print("=== Testing CRUD Operations ===") 
 
print("1. Creating a new book...") 
data = {"title": "Test Book", "author": "Test Author"} 
response = requests.post(BASE_URL, json=data) 
print("   Status:", response.status_code) 
if response.status_code == 201: 
    print("   Response:", response.json()) 
else: 
    print("   Error:", response.text) 
 
print("2. Listing all books...") 
response = requests.get(BASE_URL) 
books = response.json() 
print("   Total books:", len(books)) 
 
if books: 
    book_id = books[0]['id'] 
    print("3. Getting book ID", book_id, "...") 
    response = requests.get(f"{BASE_URL}{book_id}/") 
    print("   Status:", response.status_code) 
    if response.status_code == 200: 
        print("   Book:", response.json()) 
 
    print("4. Updating book ID", book_id, "...") 
    update_data = {"title": "Updated Title", "author": "Updated Author"} 
    response = requests.put(f"{BASE_URL}{book_id}/", json=update_data) 
    print("   Status:", response.status_code) 
    if response.status_code == 200: 
        print("   Updated:", response.json()) 
 
    print("5. Deleting book ID", book_id, "...") 
    response = requests.delete(f"{BASE_URL}{book_id}/") 
    print("   Status:", response.status_code) 
 
print("=== All tests completed ===") 
