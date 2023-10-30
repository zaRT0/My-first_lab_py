import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import os


def scrape_reviews(url, num_pages):
    if not os.path.exists("data_set"):
        
        os.makedirs("data_set")
    
    for page_num in range(1, num_pages + 1):
        
        user_agent = UserAgent().random
        
        headers = {
            "User-Agent": user_agent
        }
        
        page_url = f"{url}{page_num}"
        
        time.sleep(60)