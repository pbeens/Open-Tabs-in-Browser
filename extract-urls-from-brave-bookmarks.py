# Import the BeautifulSoup library from bs4 package.
# BeautifulSoup is a Python library for parsing HTML and XML documents.
from bs4 import BeautifulSoup

# Specify the path to the bookmarks file.
# The 'r' at the start of the file path is to ensure that the path is treated as a raw string.
bookmarks_file = r'D:\My Documents\Downloads\bookmarks_1_18_24.html'

# Define a function to extract URLs from the bookmarks file.
def extract_urls(bookmarks_file):
    # Open the bookmarks file in read mode.
    with open(bookmarks_file, 'r') as file:
        # Parse the HTML content of the file using BeautifulSoup.
        soup = BeautifulSoup(file, 'html.parser')
        # Find all <a> tags with an href attribute in the parsed HTML,
        # and create a list of the href values (i.e., the URLs).
        urls = [a['href'] for a in soup.find_all('a', href=True)]
    # Return the list of URLs.
    return urls

# Call the function to extract URLs from the bookmarks file.
urls = extract_urls(bookmarks_file)

# Print each URL.
for url in urls:
    print(url)
