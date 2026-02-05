import requests 
import json 
 
BASE_URL = "http://127.0.0.1:8000/api" 
 
print("=== Testing Authentication ===") 
 
print("1. Getting token...") 
token_response = requests.post(f"{BASE_URL}/api-token-auth/", data={"username": "admin", "password": "password123"}) 
if token_response.status_code == 200: 
    token = token_response.json()['token'] 
    print(f"   Token: {token}") 
else: 
    print(f"   Error getting token: {token_response.text}") 
    exit(1) 
 
print("2. Testing without token (should fail)...") 
response = requests.get(f"{BASE_URL}/books_all/") 
print(f"   Status without token: {response.status_code}") 
 
print("3. Testing with token (should succeed)...") 
headers = {"Authorization": f"Token {token}"} 
response = requests.get(f"{BASE_URL}/books_all/", headers=headers) 
print(f"   Status with token: {response.status_code}") 
if response.status_code == 200: 
    books = response.json() 
    print(f"   Number of books: {len(books)}") 
 
print("4. Testing book creation with token...") 
book_data = {"title": "Authenticated Book", "author": "Auth Author"} 
response = requests.post(f"{BASE_URL}/books_all/", json=book_data, headers=headers) 
print(f"   Create book status: {response.status_code}") 
if response.status_code in [200, 201]: 
    print(f"   Created book: {response.json()}") 
 
print("=== Authentication test completed ===") 
