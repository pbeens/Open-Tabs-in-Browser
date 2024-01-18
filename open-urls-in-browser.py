import os
import time
import threading
import webbrowser

# Create a new browser type for Brave
webbrowser.register('brave', None, webbrowser.GenericBrowser(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"))

# Get the new 'brave' browser type
browser = webbrowser.get('brave')

# Function to open a URL in a new tab
def open_url(url):
    browser.open_new_tab(url)

# Read URLs from a file
# Get the current working directory
current_dir = os.path.dirname(__file__)
# Create a file path that includes the current working directory
file_path = os.path.join(current_dir, 'URLs.txt')
with open(file_path, 'r') as file:
    urls = file.read().splitlines()

# Open each URL in a new tab with a pause of 0.5 seconds between them
for url in urls:
    threading.Thread(target=open_url, args=(url,)).start()
    time.sleep(1.0)
