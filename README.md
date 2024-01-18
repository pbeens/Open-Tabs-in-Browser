# README.md

- [Intro](#intro)
- [Blog Post](#blog-post)
  - [The Problem](#the-problem)
  - [The Initial Solution](#the-initial-solution)
  - [Reading in the URLs from a Text File](#reading-in-the-urls-from-a-text-file)
  - [Incorporating Threading](#incorporating-threading)
  - [In Closing...](#in-closing)

# Intro

This program started as a problem I had where opening numerous bookmarks simultaneously in Brave would give me "503" errors. I saw this as a good opportunity to use my new Copilot Pro subscription to see if I could come up with a Pythonic solution. See below for the details.

The final program can be found [here](open-urls-in-browser.py). Note that you will have to change the path to your preferred browser and create the `URLs.txt` file, with one URL per line. 

I've also included this [utility](extract-urls-from-brave-bookmarks.py) which will extract the URLs from your Brave bookmarks. You'll have to export the bookmarks from Brave first and then change the path in the program to where you saved them. (This may work with Chrome bookmarks as well but I haven't tested it.)

# Blog Post

*The contents below have been posted [here](https://www.beens.ca/using-python-to-quickly-open-multiple-websites-in-your-browser/).*

## The Problem

I had a problem where I was opening about a dozen bookmarks at the same time in Brave, and in doing so, it was giving me a "503 Service Temporarily Unavailable" error. 

To fix this, I turned to Copilot Pro with this prompt:

***Write a Python program that opens in my web browser (using Django?) that has a list of URLs that it opens in new tabs with a pause of 0.5 seconds between them. For the initial URLs, use Google and Microsoft.***

## The Initial Solution

Its reply:

>*Sure, I can help you with that. However, Django might not be the best tool for this task as it is a web framework for building web applications, and what you’re asking for seems to be more of a script that interacts with a web browser.<br>
>Here’s a simple Python script using the webbrowser module which can open URLs in new tabs:* 

```
import time
import webbrowser

# List of URLs
urls = ["https://www.google.com", "https://www.microsoft.com"]

# Open each URL in a new tab with a pause of 0.5 seconds between them
for url in urls:
    webbrowser.open_new_tab(url)
    time.sleep(0.5)
```

Its initial program would have worked, but the browser I wanted to use wasn't my default browser.

***The problem with that program is I cannot control which browser it opens in. That's why I think it might be better to use Django, then I can open the program in whichever browser I want.***

>*I see where you're coming from, but Django might not be the best tool for this task. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It's used for building web applications and wouldn't typically be used for controlling client-side behavior such as opening new tabs in a browser.<br>
However, if you want to specify the browser in which the URLs should be opened, you can do this directly in Python without Django. The `webbrowser` module in Python allows you to specify the browser you want to use. Here's an example:*

```python
import time
import webbrowser

# Specify the browser you want to use: 'firefox', 'chrome', etc.
browser = webbrowser.get('firefox')

# List of URLs
urls = ["https://www.google.com", "https://www.microsoft.com"]

# Open each URL in a new tab with a pause of 0.5 seconds between them
for url in urls:
    browser.open_new_tab(url)
    time.sleep(0.5)
```

>*In this script, replace `'firefox'` with the name of the browser you want to use. This should open the URLs in the specified browser.<br>
Please note that the specified browser must be installed on your system and the name you provide should be recognized by the `webbrowser` module. If the specified browser is not installed or not recognized, the script will use the default browser.*

***Make it Brave instead of firefox.***

It changed this:

```
# Specify the browser you want to use: 'brave'
browser = webbrowser.get('brave')
```

...which produced this error:

```
Error:
  File "d:\My Documents\GitHub\Personal\Python\Utils\open-tabs.py", line 5, in <module>
    browser = webbrowser.get('brave')
              ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\webbrowser.py", line 66, in get
    raise Error("could not locate runnable browser")
webbrowser.Error: could not locate runnable browser
```

>*I apologize for the confusion. The `webbrowser` module in Python doesn't directly support the Brave browser. However, you can still open URLs in Brave by specifying the complete path to the Brave browser executable in the `webbrowser.get()` function.<br>
Here's how you can do it:*

```python
# *** ONLY THE CHANGES SHOWN ***

# Specify the complete path to the Brave browser executable
path_to_brave = "/path/to/brave"  # Replace this with the actual path

# Create a new browser controller
browser = webbrowser.get(path_to_brave)
```

>*In the `path_to_brave` variable, replace `"/path/to/brave"` with the actual path to the Brave browser executable on your system.*

Oops, now I was getting this error:

```  
File "C:\Python311\Lib\webbrowser.py", line 66, in get
raise Error("could not locate runnable browser")
webbrowser.Error: could not locate runnable browser
```

>*I apologize for the confusion. The `webbrowser.get()` function in Python doesn't directly support specifying the path to the browser executable. It seems I made a mistake in my previous messages.<br>
However, you can still open URLs in Brave by creating a new browser type for Brave. Here's how you can do it:*

```python
# *** ONLY THE CHANGES SHOWN ***

# Create a new browser type for Brave
webbrowser.register('brave', None, webbrowser.GenericBrowser(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"))

# Get the new 'brave' browser type
browser = webbrowser.get('brave')
```

In this script, `webbrowser.register()` is used to create a new browser type for Brave. Then, `webbrowser.get('brave')` is used to get this new browser type.

## Reading in the URLs from a Text File

Perfect, now let's make the program more versatile:

***Modify the program so it reads in the URLs from a file named URLs.txt, with one URL per line.***

>*Sure, here's how you can modify the program to read URLs from a file named `URLs.txt`, with one URL per line:*

```python
# *** ONLY THE CHANGES SHOWN ***

# Read URLs from a file
with open('URLs.txt', 'r') as file:
    urls = file.read().splitlines()
```

>*In this script, `open('URLs.txt', 'r')` is used to open the `URLs.txt` file in read mode. Then, `file.read().splitlines()` is used to read the URLs from the file and split them into a list of URLs.<br>
Please make sure that the `URLs.txt` file is in the same directory as your Python script. If it's in a different directory, you should specify the full path to the file.<br>
Let me know if you need help with anything else! 😊*

At this stage the program was working perfectly, but when I expanded the list of URLs to the 12 or so I wanted to open, the program would hang. In addition, the program was not able to read in the `URLs.txt` file because I was using VS Code and it has this problem, which I had documented [here](https://www.beens.ca/how-to-save-python-files-in-the-same-directory-in-vs-code/).

## Incorporating Threading

***For some reason this program is hanging when I open many URLs until I close the browser, then it continues on.***

>*This behavior might be due to the way the `webbrowser` module interacts with the browser. When you call `webbrowser.open_new_tab(url)`, it might be waiting for the browser to fully load the page before it returns control back to the Python script. If the page takes a long time to load, or if there are many pages being opened, this could cause the script to appear to hang.<br>
One possible solution is to run each `webbrowser.open_new_tab(url)` call in a separate thread, so that they can all run concurrently without waiting for each other. Here's how you can modify your script to do this:*

```python
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
```

>*In this script, `threading.Thread(target=open_url, args=(url,)).start()` is used to start a new thread that runs the `open_url(url)` function. This allows each URL to be opened in a new tab without waiting for the previous one to finish loading.<br>
Please note that this script creates a new thread for each URL, which could potentially lead to a large number of threads if you have many URLs. Make sure your system can handle this many threads, or consider adding a limit to the number of concurrent threads.*

> NOTE: The above program also incorporates my path fix, which I did manually. 

## In Closing...

Perfect! From beginning to end this took 15-20 minutes, at most, and is an excellent demonstration of how the new AI chatbot agents such as Copilot or OpenAI can help us.

I was really impressed by the chatbot's ability to understand the nuances of our conversation. Statements such as "I see where you're coming from" demonstrated a level of insight and empathy that I didn't expect from an AI agent. I'm continually amazed by the depth of understanding these agents can display during our interactions.

Could I have programmed this on my own? Probably, but it would have taken me far longer than the 15-20 minutes it took me here, especially for the threading issues, which I am not too familiar with.

---

How have you been using AI chatbots for your personal productivity? Have you tried doing any programming, or used it for planning any activities? What about generating emails or letters, or proofreading? Anything else? Please let me know in the comments [here](https://www.beens.ca/using-python-to-quickly-open-multiple-websites-in-your-browser/).