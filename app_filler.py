#import Beutiful Soup
from bs4 import BeautifulSoup
import requests


#retreive url to search
page_url = input("Enter URL: ")


#requests page through User Agent Mozilla
page_response = requests.get(page_url, timeout=5,  headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page_response.content, "html.parser")

print(soup.prettify())



