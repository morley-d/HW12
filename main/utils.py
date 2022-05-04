import json
import app


def load_json_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts_by_substring(substring):
    posts = load_json_data(app.POST_PATH)
    posts_founded = []
    for post in posts:
        if substring.lower() in post['content'].lower():
            posts_founded.append(post)
    return posts_founded

print(search_posts_by_substring("елк"))
