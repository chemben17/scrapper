import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

#This is to make sure the url only appear once in our crawling nad not multiple times
visited_urls = set()

def spider_url(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url} Check the url and  try again")
        return
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        a_tags = soup.find_all('a')
        urls = []
        for a_tag in a_tags:
            a_tag = a_tag.get('href')
            if a_tag is not None and a_tag != "":
                urls.append(a_tag)
        # print(urls)

        for i in urls:
            if i not in visited_urls:
                visited_urls.add(i)
                url_join = urljoin(url, i)
                if keyword in url_join:
                    print(url_join)
                    with open("../../venv/scrapped.txt", "a") as file:
                        file.write(url_join + "\n")
                    spider_url(url_join, keyword)
                else:
                    pass



url = input("Enter the uel you want to scrape: ")
keyword = input("Enter the keyword to search for in the URL provided")
spider_url(url, keyword)


# https://www.coursera.org/articles/programmer-vs-developer
#https://mktoevents.com/Microsoft+Event/399854/157-GQE-382?wt.mc_id=AID3061954_QSG_PD_SCL_645575&OCID=AID3061954_PSOC_30427418_373613168_196785845