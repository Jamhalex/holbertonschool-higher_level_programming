#!/usr/bin/env python3
"""
Module to fetch posts from JSONPlaceholder using requests,
print titles, and save selected fields to a CSV file.
"""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints:
    - Status code
    - Titles of all posts (if successful)
    """
    response = requests.get(URL, timeout=10)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them into posts.csv
    with columns: id, title, body (if successful).
    """
    response = requests.get(URL, timeout=10)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
