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
print("")

# count total "posts"
total_posts = len(posts)
print("Total posts: ", total_posts)
print("")

#Count total posts done by Leanne
Leanne_posts = []

for post in posts:
    if post["userId"] == Leanne_id:
        Leanne_posts.append(post)
her_posts = len(Leanne_posts)

#test
print(f"Leanne Graham has {her_posts} posts.")
print("")

# Print Leanne's post titles
print("\t Leanne's post's are: ")
print("\t --------------------")

counter = 1
for post in Leanne_posts:
    print(f" \t {counter}. {post['title']}")
    counter += 1