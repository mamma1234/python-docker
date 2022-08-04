from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
# s = Service(CHROMEDRIVER_PATH)
# browser = webdriver.Chrome(service=s)
# url = 'https://www.google.com'
# browser.get(url)


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")
