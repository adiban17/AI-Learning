'''
Real-World Example: Multithreading for I/O bound tasks,
Scenario: Web Scarping
Web Scraping often involves making numerous I/O requests to fetch web pages.
These tasks are I/O bound as they take a ot of time waiting for responses from servers. Multithreading can significantly improve the performance by 
allowing multiple web pages to be scarped simultaneously.
'''

import threading
import requests
from bs4 import BeautifulSoup

link="https://www.latent.space/p/2025-papers?ref=dailydev"

def get_content(link):
    response=requests.get(link)
    soup=BeautifulSoup(response.content,'html.parser')
    print(soup.text)

get_content(link)
