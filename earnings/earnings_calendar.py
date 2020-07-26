import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import os

userProfile = "C:\\Users\\" + 'alex' + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument("user-data-dir={}".format(userProfile))
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
options.add_argument(f'user-agent={userAgent}')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://marketchameleon.com/Calendar/Earnings')



# import requests
# from bs4 import BeautifulSoup

# url = "https://marketchameleon.com/Calendar/Earnings"

# session = requests.Session()

# r = session.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
