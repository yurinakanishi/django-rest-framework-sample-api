from collections import Counter
import json


def run():
    data = json.load(open("a.json"))

    slug_counter = Counter(item["slug"] for item in data)

    for slug, count in slug_counter.items():
        if count > 1:
            print(f"'{slug}' appears {count} times")
