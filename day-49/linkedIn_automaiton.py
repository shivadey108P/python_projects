from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.common.exceptions import StaleElementReferenceException

# Load environment variables
load_dotenv()

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

# Chrome options setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-webrtc")
chrome_options.add_argument("--disable-rtc-smoothing")
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# XPaths for elements
msg_close_button = (By.XPATH, "//button[contains(@class, 'msg-overlay-bubble-header__control')][2]")
dropdown_select_job = (By.XPATH, "//button[text()= 'python developer']")
easy_apply = (By.XPATH, "//button[text()= 'Easy Apply']")
experience_level_button = (By.XPATH, "//button[text()='Experience level']")
entry_level_option = (By.XPATH, "//span[text()='Entry level']")
associate_option = (By.XPATH, "//span[text()='Associate']")
show_results_experience_button = (By.XPATH, "//*[text()='Filter results by: Experience level']//following::button[2]")
list_of_job_results = (By.XPATH, "//ul[@class='scaffold-layout__list-container']/li")
jobs_save_button = (By.XPATH, "//span[@class='visibility-hidden']//following::span[text()='Save'][1]")
company_name = (By.XPATH, "//div[@class='job-details-jobs-unified-top-card__company-name']/a")
employee_count = (By.XPATH, "//span[@class='t-normal t-black--light link-without-visited-state link-without-hover-state']")
confirmation_saved_job = (By.XPATH, "//span[text()='You’ve saved this job.']")
save_job_close_btn = (By.XPATH, "//button[contains(@aria-label,'Dismiss “You’ve saved this job.” notification 1 of ')]")

# Helper functions
def wait_for_element(driver, element, timeout=60):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(element)
    )

def quit_browser(driver):
    driver.quit()

def safe_click(driver, locator):
    attempt = 0
    while attempt < 3:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            break
        except StaleElementReferenceException:
            attempt += 1
            time.sleep(2)  # Adding a slight delay before retrying
        except Exception as e:
            print(f"Error: {str(e)}")
            break

# Maximize window
driver.maximize_window()

# Open LinkedIn and sign in
driver.get('https://www.linkedin.com/')
wait_for_element(driver, element=(By.LINK_TEXT, 'Sign in'))

driver.find_element(By.LINK_TEXT, value='Sign in').click()
driver.find_element(By.ID, value='username').send_keys(email)
driver.find_element(By.ID, value='password').send_keys(password)
driver.find_element(By.XPATH, value="//button[contains(text(),'Sign in')]").click()

# Navigate to Jobs section
wait_for_element(driver, element=(By.XPATH, "//span[text()='Jobs']"))
time.sleep(2)

driver.find_element(*msg_close_button).click()
time.sleep(2)
driver.find_element(By.XPATH, value="//span[text()='Jobs']").click()

# Job search
wait_for_element(driver, element=(By.XPATH, "//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-global-typeahead__input']"))
time.sleep(2)
driver.find_element(By.XPATH, value="//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-global-typeahead__input']").send_keys('Python Developer')

# Select job and location
wait_for_element(driver=driver, element=dropdown_select_job)
time.sleep(2)
driver.find_element(*dropdown_select_job).click()

wait_for_element(driver=driver, element=(By.XPATH, "//input[@class='jobs-search-box__text-input jobs-search-box__text-input--with-clear']"))
time.sleep(3)
location = driver.find_element(By.XPATH, value="//input[@class='jobs-search-box__text-input jobs-search-box__text-input--with-clear']")
location.clear()
time.sleep(2)
location.send_keys('Hyderabad', Keys.DOWN, Keys.ENTER)

time.sleep(3)

# Filter by experience level
driver.find_element(*experience_level_button).click()
time.sleep(1)

driver.find_element(*entry_level_option).click()
time.sleep(2)

driver.find_element(*associate_option).click()
time.sleep(2)

driver.find_element(*show_results_experience_button).click()
time.sleep(3)

driver.find_element(*easy_apply).click()
time.sleep(5)

list_of_jobs = driver.find_elements(*list_of_job_results)

count = 1

save_job = False

# Loop through job listings
for _ in list_of_jobs:
    try:
        wait_for_element(driver=driver, element=(By.XPATH, f"//ul[@class='scaffold-layout__list-container']/li[{count}]"))
        current_job = driver.find_element(By.XPATH, value=f"//ul[@class='scaffold-layout__list-container']/li[{count}]")
        time.sleep(2)
        current_job.click()

        # Safe click implementation for company name
        safe_click(driver, company_name)

        wait_for_element(driver=driver, element=employee_count)
        time.sleep(3)
        count_of_employee = driver.find_element(*employee_count).text.strip()
        if '10K+ employees' in count_of_employee:
            save_job = True
        else:
            save_job = False
        driver.back()
        wait_for_element(driver=driver, element=company_name)
        time.sleep(3)
        if save_job:
            safe_click(driver, jobs_save_button)
            time.sleep(2)
            driver.find_element(*save_job_close_btn).click()
        time.sleep(2)

        count += 1

    except Exception as e:
        print(f"An error occurred for job {count}: {str(e)}")
        count += 1
        continue

quit_browser(driver)
