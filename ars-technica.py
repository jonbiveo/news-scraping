from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

service = Service("/home/jonbiveo/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://arstechnica.com/')

postings = []
# .article header > h2 > a
for post in driver.find_elements(By.XPATH, '//*[@id="main"]/section[1]/ul/li'):
    title = post.find_element(By.XPATH, './/header/h2/a').text
    img = post.find_element(By.XPATH, './/figure/div').value_of_css_property('background-image')
    img_url = re.split('[""]',img)[1]
    description = post.find_element(By.XPATH, './/header/p').text

    post_item = {
        'title': title,
        'img': img_url,
        'description': description
    }

    postings.append(post_item)

df = pd.DataFrame(postings)
print(df)

#test