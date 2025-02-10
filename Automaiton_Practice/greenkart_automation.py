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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(3)
all_products = driver.find_elements(By.CSS_SELECTOR, "div .product .product-name")
products_to_purchase = []
for product in all_products:
    products_to_purchase.append(product.text)

add_to_cart_btns = driver.find_elements(
    By.CSS_SELECTOR, "div .product  .product-action button"
)
for btn in add_to_cart_btns:
    btn.click()

no_of_items = driver.find_element(
    By.XPATH, "//td[text()='Items']//following::strong[1]"
).text
assert len(products_to_purchase) == float(no_of_items), (
    "No of items in cart and selected doesn't match!"
)

price_in_home_screen = float(
    driver.find_element(By.XPATH, "//td[text()='Price']//following::strong[1]").text
)

driver.find_element(By.CLASS_NAME, "cart-icon").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CLASS_NAME, "promoBtn").click()

product_name_in_checkout = driver.find_elements(By.CSS_SELECTOR, "td .product-name")

products_in_checkout = []

for product in product_name_in_checkout:
    products_in_checkout.append(product.text)

assert len(products_in_checkout) == len(products_to_purchase), (
    "Incorrect number of products in checkout!"
)

for product in products_to_purchase:
    if product not in products_in_checkout:
        assert 1 == 0, f"Product {product} was not found during checkout!"

wait = WebDriverWait(driver, 15)

wait.until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo"))
)

total_amt_in_checkout = float(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert price_in_home_screen == total_amt_in_checkout, (
    "Total amount does not match in home screen and during checkout!"
)

amt_after_discount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

assert total_amt_in_checkout > amt_after_discount, "Discount is not applied properly!"

percent_value = driver.find_element(By.CLASS_NAME, "discountPerc").text

discount_percent = int(percent_value.split("%")[0])

discount_amount_calculated = total_amt_in_checkout - (
    total_amt_in_checkout / discount_percent
)

assert discount_amount_calculated == amt_after_discount, (
    "discount amount not calculated properly!"
)

print("--------------------------------------------------------------")
print("-----------------Automation Success!--------------------------")
print("--------------------------------------------------------------")

driver.quit()
