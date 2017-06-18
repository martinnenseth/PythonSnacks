import webbrowser
import sys
from selenium import webdriver



def visist_site(url):
    counter = 0
    while True:
        webbrowser.open(url)
        counter += 1
        print(counter)

if __name__ == "__main__":
    visist_site('https://www.youtube.com/watch?v=noo2Y6mKxnE')