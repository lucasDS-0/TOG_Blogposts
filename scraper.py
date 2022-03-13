import requests
from bs4 import BeautifulSoup

URL = ""

def get_URL(url_path):
    return requests.get(url_path)

