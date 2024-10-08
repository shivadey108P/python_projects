from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.in/LG-Inverter-Fully-Automatic-Washing-FHM1207SDM/dp/B0BMGD9Y2X/ref=sr_1_2_sspa")

try:
    # Wait for the price container to be visible first
    price_container = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'a-section a-spacing-none')]"))
    )
    
    # Then, retrieve the price within the container
    product_price = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='aok-offscreen']//following::span[@class='a-price-whole'][1]"))
    ).text
    
    print(f"Product price: {product_price}")
    
finally:
    driver.quit()
