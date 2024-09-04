from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os

load_dotenv()

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/')

driver.find_element(By.LINK_TEXT, value='Sign in').click()

driver.find_element(By.ID, value='username').send_keys(email)

driver.find_element(By.ID, value='password').send_keys(password)

driver.find_element(By.XPATH, value="//button[contains(text(),'Sign in')]").click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Jobs']"))
)

driver.find_element(By.XPATH, value="//span[text()='Jobs']").click()

driver.find_element(By.XPATH, value="//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-global-typeahead__input']").send_keys('Python Developer')

driver.find_element(By.XPATH, value="//input[@class='jobs-search-box__text-input']").send_keys('Hyderabad', Keys.Enter)