from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-popup-blocking")
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME, "blinkingText").click()

windows_available = driver.window_handles

driver.switch_to.window(windows_available[1])

wait.until(
    expected_conditions.presence_of_element_located(
        (By.XPATH, "//p[@class='im-para red']")
    )
)

red_text = driver.find_element(By.XPATH, "//p[@class='im-para red']").text

email = ""

text = red_text.split()

for word in text:
    if "@" in word:
        email = word

print(email)

driver.close()

driver.switch_to.window(windows_available[0])

driver.find_element(By.ID, "username").send_keys(email)

driver.find_element(By.ID, "password").send_keys("learning")

driver.find_element(By.ID, "terms").click()

driver.find_element(By.ID, "signInBtn").click()

wait.until(
    expected_conditions.presence_of_element_located(
        (
            By.XPATH,
            "//div[@class='alert alert-danger col-md-12' and @style='display: block;']",
        )
    )
)

incorrect_details_msg = driver.find_element(
    By.XPATH,
    "//div[@class='alert alert-danger col-md-12' and @style='display: block;']",
).text

assert incorrect_details_msg == "Incorrect username/password.", (
    "The error message was not displayed!"
)

print(incorrect_details_msg)

driver.quit()
