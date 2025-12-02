#!/usr/bin/python3
"""nadfigvbiadfhvbdf"""

import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Iterate through posts and print titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Structure data into a list of dictionaries
        structured_posts = []
        for post in posts:
            structured_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        
        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
