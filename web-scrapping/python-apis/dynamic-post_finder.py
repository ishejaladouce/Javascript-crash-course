# We import the requests library to fetch data from the internet (API)
import requests

# We get all the users and posts data from the given URLs
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

# We greet the user
print("Welcome to the Post Finder!")

# We keep looping until the user decides to exit
while True:
    # We show the main menu
    print("\nWhat would you like to do?")
    print("1. Find posts")
    print("2. Exit")

    # We ask for user choice
    choice = input("> ")

    # If the user chooses to find posts
    if choice == "1":
        # We count and show how many users are available
        total_users_count = len(users)
        print(f"\nThere are {total_users_count} users, and they are:")

        count = 1
        for user in users:
            print(f"\t{count}. {user['name']}")
            count += 1

        # We ask which user they want to see posts for
        chosen_name = input("\nWhose posts would you like to see?\n(Type the name exactly as shown)\n\t>> ").strip()

        # We check if the entered name exactly matches one of the users
        selected_user = None
        for user in users:
            if user["name"] == chosen_name:  # case-sensitive match
                selected_user = user
                break

        # If we found a user, we show their posts
        if selected_user:
            user_id = selected_user["id"]
            user_posts = []

            # We collect all posts made by that user
            for post in posts:
                if post["userId"] == user_id:
                    user_posts.append(post["title"])

            total_userPosts_count = len(user_posts)
            print(f"\n{selected_user['name']} has {total_userPosts_count} total posts:")
            print("The posts are:")

            count = 1
            for title in user_posts:
                print(f"\t{count}. {title}")
                count += 1

        # If the name doesn’t match exactly, we show a message
        else:
            print("\nThe name you entered doesn’t match exactly.")
            print("Please type the name exactly as it appears in the list above (including capital letters).")

    # If the user chooses to exit
    elif choice == "2":
        print("\nGoodbye!")
        break

    # If they type something invalid
    else:
        print("\nInvalid choice. Please choose 1 or 2.")
