import requests

user_response = requests.get("https://jsonplaceholder.typicode.com/users")
post_response = requests.get("https://jsonplaceholder.typicode.com/posts")

users = user_response.json()
posts = post_response.json()

# print(f"{posts}")

#  find Leanne's Id

Leanne_id = None
for user in users:
    if user["name"] == "Leanne Graham":
        Leanne_id = user["id"]
        break

# Count total post 
total_posts = len(posts)

print(f"The total posts made are: {total_posts}")

#count total posts made by Leanne
Leanne_posts = []
for post in posts:
    if post["userId"] == Leanne_id:
        Leanne_posts.append(post)
her_posts = len(Leanne_posts)

print(f"The total posts done by Leanne are: {her_posts}")

#print the title of posts done by Leanne

counter = 1
for post in Leanne_posts:
    print(f"\t{counter}. {post['title']}")
    counter += 1