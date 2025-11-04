import requests

users_response = requests.get("https://jsonplaceholder.typicode.com/users")
posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")

users = users_response.json()
posts = posts_response.json()

Leanne_id = None
for user in users:
    if user["name"] == "Leanne Graham":
        Leanne_id = user["id"]
        break

#test  the codes if fetching the id for Leanne
print("Leanne Graham user id: ", Leanne_id)

# count total posts
total_posts = len(posts)
print("Total posts: ", total_posts)

