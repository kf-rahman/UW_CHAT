from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode for automation

# Initialize WebDriver
driver = webdriver.Chrome()

# URL to scrape
url = 'https://uwaterloo.ca/academic-calendar/undergraduate-studies/catalog#/programs/rJj6aXDk6'
driver.get(url)

# Wait for JavaScript to render the page
time.sleep(5)  # Adjust timing according to the page's response time

# Extracting structured data
try:
    sections = driver.find_elements(By.CSS_SELECTOR, 'div.program-view__pre___1zoJ6')
    for section in sections:
        header = section.find_element(By.CSS_SELECTOR, 'div.style__itemHeaderH2___3U8zB span').text
        items = section.find_elements(By.CSS_SELECTOR, 'ul > li')
        for item in items:
            description = item.find_element(By.CSS_SELECTOR, 'div[data-test]').text
            print(f"Header: {header}")
            print(f"Description: {description}")
finally:
    driver.quit()
