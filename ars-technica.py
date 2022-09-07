from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

service = Service("/home/jonbiveo/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://arstechnica.com/')

for post in driver.find_elements(By.CLASS_NAME, 'tease.article'):
    title = post.find_element(By.CSS_SELECTOR, '.article header > h2 > a').text
    print(title)