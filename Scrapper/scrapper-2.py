import sys
import requests


# Define a function named 'urls' that takes an 'out_file' parameter.
def urls(out_file):
    # Read a list of URLs from standard input and split them into lines.
    urls2 = sys.stdin.read().splitlines()

    # Create two empty lists to store good and bad URLs.
    good_urls = []
    bad_urls = []

    # Iterate through each URL in the 'urls2' list.
    for url in urls2:
        try:
            response = requests.head(url)

            if response.status_code == 200:
                good_urls.append(url)
        except requests.exceptions.MissingSchema:
            bad_urls.append(url)
            continue
        except requests.exceptions.ConnectionError:
            bad_urls.append(url)
            continue
    with open(out_file, 'a') as file:
        file.write('\n'.join(good_urls))

    print(f"Saved URLS {out_file}")


out_file = 'filtered_urls.txt'


urls(out_file)

#
# import sys
# import requests
#
# def urls(out_file):
#     io = sys.stdin.read().splitlines()
#
#     for i in io:
#         try:
#             sy = requests.head(url)
#
#             if sy.status_code == 200:



