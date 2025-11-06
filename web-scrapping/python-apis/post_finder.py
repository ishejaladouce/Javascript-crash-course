import requests

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

print("\nWelcome to the post finder!")

total_users_count = len(users)
print(f"\nWe have {total_users_count} total users, and they are:")

count = 1
for user in users:
    user_name = user['name']
    print(f"\t{count}. {user_name}")
    count += 1

chosen_name = input("\nWhose posts would you like to see?\n\t >>")

selected_user = None
for user in users:
    if user['name'] == chosen_name:
        selected_user = user
        break

if selected_user:
    user_id = selected_user['id']
    user_posts = []

    for post in posts:
        if post['userId'] == user_id:
            user_posts.append(post['title'])

    total_userPosts_count = len(user_posts)
    print(f"\n{chosen_name} has {total_userPosts_count} total posts;")
    print("The posts are:")

    count = 1
    for title in user_posts:
        print(f"\t{count}. {title}")
        count += 1

else:
    print("User not found. Please check the name and try again.")