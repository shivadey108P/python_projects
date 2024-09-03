from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cookie_page import CookiePage
import time

timeout = time.time() + 5
five_min = time.time() + 60*5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

cookie = CookiePage(driver=driver)

cookie.get_url("https://orteil.dashnet.org/experiments/cookie/")


while time.time() < five_min:
    cookie.wait_for_element(cookie.cookie)
    cookie.click_cookie()
    
    
    
cookie.quit_browser()



