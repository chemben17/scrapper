# https://www.coursera.org/articles/programmer-vs-developer

import requests
#request module helps the interaction with HTTP smooth when it comes with interacting with the web
from bs4 import BeautifulSoup as bs

def get_page(url) :
    # the requests.get allows us to specify what we want to interact on with HTTp
    response = requests.get(url)

    soup = bs(response.content, 'html.parser')

    vars = (soup.find_all('a'))

    for var in vars:
        print(var.get("href"))

your_url = input("What URL would you love to scrape? ")
get_page(your_url)
