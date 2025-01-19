import requests
from bs4 import BeautifulSoup


def get_page(url_path):
    return requests.get(url_path)


def parse_page(page):
    parsed = BeautifulSoup(page.content, "html.parser")
    return parsed


def get_blogpost(parsed_page):
    header = parsed_page.find(id="Blog_Post")
    header = header.parent.next_sibling
    return header.find_next()

def print_blogpost(blogpost):
    print("SIU's Blogpost:")
    print()
    print(blogpost.text.strip())
    print()
