# Count posts made by user id 1 (Lean)
# Print the title of each post
import json

with open("posts.json", "r") as file:
    posts = json.load(file)

counter = 0
for item in posts:
    if item["userId"] == 1:
        counter += 1
print(counter)
    