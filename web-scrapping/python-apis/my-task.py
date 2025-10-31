import json

with open("posts.json", "r") as posts_file:
    posts = json.load(posts_file)

with open("users.json", "r") as users_file:
    users = json.load(users_file)

user_id = None
for user in users:
    if user["name"] == "Leanne Graham":
        user_id = user["id"]
        break

counter = 0
for post in posts:
    if post["userId"] == user_id:
        counter += 1

print(f"Leanne Graham with Id: {user_id} has {counter} posts.")