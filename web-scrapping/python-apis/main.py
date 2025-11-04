import requests

users_response = requests.get("https://jsonplaceholder.typicode.com/users")
posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")

users = users_response.json()
posts = posts_response.json()

