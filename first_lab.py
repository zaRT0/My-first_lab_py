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
        
        response = requests.get(page_url, headers=headers)
        if response.status_code == 200:
            print("Successfully!")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            review_links = soup.find_all('a', class_='review-title')
            rate = soup.find_all('div', class_='product-rating tooltip-right')
            
            for title, rating in zip(review_links, rate):
                
                rating_text = rating['title']
                
                star_rating = rating_text[-1]
                
                review_txt = title.text
                
                rating_folder = os.path.join("data_set", star_rating)
                
                if not os.path.exists(rating_folder):
                    os.makedirs(rating_folder)
                
                files_in_folder = os.listdir(rating_folder)
                
                file_number = len(files_in_folder) + 1
                
                file_name = f"{file_number:04d}.txt"