import json

with open("users.json", "r") as users_file:
    users = json.load(users_file)

with open("posts.json", "r") as posts_file:
    posts = json.load(posts_file)

print(f"There are {len(users)} users.\n")

for user in users:
    user_id = user["id"]
    user_name = user["name"]

    user_posts = [post for post in posts if post["userId"] == user_id]

    print(f"User {user_name} has {len(user_posts)} posts")
    if user_posts:  
        print("Her/His posts are:")
        for i, post in enumerate(user_posts, start=1):
            print(f"  {i}. {post['title']}")
    print("\n") 
