#!/usr/bin/python3
import csv
import requests


def fetch_and_print_posts():
    """
    fetches and prints all posts from JSON placeholder URL
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for data in posts:
            print(data['title'])


def fetch_and_save_posts():
    """
    fetches and saves all posts from JSON placeholder URL
    to CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_data = []

        for post in posts:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_data.append(post_dict)

        with open('posts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)
