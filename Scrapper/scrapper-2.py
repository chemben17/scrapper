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
        # Send an HTTP HEAD request to the URL.
        try:
            response = requests.head(url)
            # Check if the response status code is 200 (OK).

            if response.status_code == 200:
                # If the status code is 200, add the URL to the 'good_urls' list.

                good_urls.append(url)
        except requests.exceptions.MissingSchema:
            # If there's a 'MissingSchema' exception (e.g., URL lacks http://), add the URL to 'bad_urls'.
            bad_urls.append(url)
            continue
        except requests.exceptions.ConnectionError:
            # If there's a 'ConnectionError' (e.g., failed to connect to the URL), add the URL to 'bad_urls'.
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



