from collections import Counter
import json

data = json.load(open("auto_movies.json"))


slug_counter = Counter(item["slug"] for item in data)

for slug, count in slug_counter.items():
    if count > 1:
        print(f"'{slug}' appears {count} times")
