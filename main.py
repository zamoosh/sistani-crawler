from bs4.element import Tag
from bs4 import BeautifulSoup
from requests import Response
import requests
import re


class Crawler:
    URL_REGEX = re.compile(r".*(\d+/\d+)/")
    BASE_URL = "https://www.sistani.org"
    URL_LIST = [
        "https://www.sistani.org/persian/book/26575/",
        "https://www.sistani.org/persian/book/26576/",
        "https://www.sistani.org/persian/book/26577/",
        "https://www.sistani.org/persian/book/26578/",
    ]


