from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys('Shiva')

last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys('Dey')

email = driver.find_element(By.NAME, value='email')
email.send_keys('shiva.dey@gmail.com')

sign_up_button = driver.find_element(By.XPATH, value="//button[text()='Sign Up']")
sign_up_button.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "display-3"))
)
display_text_h1 = driver.find_element(By.CLASS_NAME, value='display-3')
if display_text_h1.text == 'Success!':
    print('Success')
    
driver.quit()