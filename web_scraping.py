from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: runs without opening a browser window

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.geeksforgeeks.org/html-introduction/'

# Open the URL
driver.get(url)

# Wait for content to load (optional but can help in some cases)
sleep(3)

# Get the page source after JavaScript is rendered
html = driver.page_source

# Now parse the page with BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Print the entire text content of the page
print(soup.get_text(separator='\n', strip=True))

# Close the driver
driver.quit()
