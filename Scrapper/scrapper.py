import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin

# This is to make sure the url only appear once in our crawling nad not multiple times
visited_urls = set()


def spider_url(url, keyword):
    try:
        response = requests.get(url)
    except:
        # to make sure the url is valid
        print(f"Request failed {url} Check the url and  try again")
        return
    # if the url is active
    if response.status_code == 200:
        soup = BS(response.content, 'html.parser')
        # anchor tags are scrapped and store as a list
        a_tags = soup.find_all('a')

        # an empty list to store the urls scrapped
        urls = []

        # Iterates throught the elements of the a_tags list
        for a_tag in a_tags:
            # the href attribute in each anchor a-tags is scrapped
            a_tag = a_tag.get('href')
            # check if there's invalid or empty href
            if a_tag is not None and a_tag != "":
                # valid urls are appended into the URLS list created
                urls.append(a_tag)
        # print(urls)

        #  Iterates through the elements of urls list
        for i in urls:
            # check if elements of urls are not already stored in the Visited_urls list
            if i not in visited_urls:
                visited_urls.add(i)

                # joins the i elements to the url
                url_join = urljoin(url, i)

                # check if the keyword is in the absolute url
                if keyword in url_join:
                    print(url_join)

                    # opens / creates a new file and store the each elements of url_join
                    with open("../../venv/scrapped.txt", "a") as file:
                        file.write(url_join + "\n")
                    spider_url(url_join, keyword)
                else:
                    pass


url = input("Enter the uel you want to scrape: ")
keyword = input("Enter the keyword to search for in the URL provided")
spider_url(url, keyword)


# https://www.coursera.org/articles/programmer-vs-developer
# https://mktoevents.com/Microsoft+Event/399854/157-GQE-382?wt.mc_id=AID3061954_QSG_PD_SCL_645575&OCID=AID3061954_PSOC_30427418_373613168_196785845
