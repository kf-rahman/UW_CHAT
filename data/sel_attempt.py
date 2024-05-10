from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set the path to the ChromeDriver
driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=chrome_options)

# URL you want to scrape
url = 'https://uwaterloo.ca/academic-calendar/undergraduate-studies/catalog#/programs/rJj6aXDk6'
driver.get(url)

# Get all text in body or specific elements
text = driver.find_element_by_tag_name('body').text

print(text)  # Prints the entire text content of the page

# Clean up (close the browser)
driver.quit()
