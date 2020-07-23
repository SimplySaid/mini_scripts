import pickle
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Delay for selenium to wait for element to load
DELAY = 10

#Twitch Login - Only need to enter once to save cookies to pickle
USERNAME = ''
PASSWORD = ''

CHANNEL = 'loltyler1' #Channel to Crawl

#Twitch API Configuration
TWITCH_API_ENDPOINT = 'https://api.twitch.tv/kraken/streams/'
API_HEADERS = {
    'Client-ID' : 'enmt69fvr2kpgubpw96ny2f6fbv9wg',
    'Accept' : 'application/vnd.twitchtv.v5+json',
}

#Gets Twitch Channel ID using the Channel Name
def get_channel_id (channel):
    r = requests.get("https://api.twitch.tv/kraken/users?login=" + channel, headers = API_HEADERS)
    channeljson = r.json()
    id = channeljson['users'][0]['_id']
    return id

#Pickles your login function so you don't have to enter authentication everytime
def login (un, pw):
    driver = webdriver.Chrome()
    driver.get("http://www.twitch.tv/" + CHANNEL)
    #login_button = driver.find_element_by_class_name("tw-pd-x-05")
    login_menu = driver.find_element_by_xpath("//button[@data-a-target='login-button']")
    login_menu.click()
    try:
        username_box = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, "login-username")))
        password_box = driver.find_element_by_id("password-input")
        username_box.send_keys(USERNAME)
        password_box.send_keys(PASSWORD)
        login_btn = driver.find_element_by_xpath("//button[@data-a-target='passport-login-button']").click()

    except:
        print('Login Failed')
        return

    #Sleep for 60 seconds to give enough time to enter captcha + authentication
    time.sleep(60)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

#Loads Cookies into Browser so you don't have to relogin everytime
def load_cookies(driver):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    driver.delete_all_cookies()
    driver.get("http://www.twitch.tv/" + CHANNEL)
    for cookie in cookies:
        driver.add_cookie(cookie)

#Checks if channel is live using TwitchAPI
def check_live(channel):
    r = requests.get(TWITCH_API_ENDPOINT + channel, headers = API_HEADERS)
    jsondata = r.json()
    if 'stream' in jsondata:
        if jsondata['stream'] is not None:
            return True
        else:
            return False

#Collects Twitch Channel Points
def collect_points(driver):
    try:
        rewards_button = WebDriverWait(driver, DELAY).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='tw-button tw-button--success tw-interactive']")))
        rewards_button.click()
        print('Points Collected')
    except:
        print('Rewards Not Available')

#Checks if Driver has been closed
def check_browser_active(driver):
    try:
        driver.title
        return True
    except:
        return False
    
    print(driver.getTitle)

#Reloads Browser / Driver
def load_browser():
    driver = webdriver.Chrome()
    driver.get("http://www.twitch.tv/" + CHANNEL)
    load_cookies(driver)
    driver.get("http://www.twitch.tv/" + CHANNEL)

    return driver

def main():
    channel_id = get_channel_id(CHANNEL)
    web_driver = load_browser()
    while True:
        if check_live(channel_id) == True:
            if check_browser_active(web_driver) == False:
                load_browser()
            collect_points(web_driver)
        else:
            web_driver.quit()
            print('Stream Not Live, Driver Closed')

        time.sleep(300)

main()
#login(USERNAME, PASSWORD)

