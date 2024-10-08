from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

timeout = time.time() + 5
five_min = time.time() + 60 * 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

cookie = (By.ID, 'cookie')
upgrades = (By.CSS_SELECTOR, '#store div')
money = (By.ID, 'money')
cps = (By.ID, 'cps')
all_prices = (By.CSS_SELECTOR, '#store b')

def wait_for_element(driver, element, timeout=60):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(element)
    )

def quit_browser(driver):
    driver.quit()

driver.maximize_window()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

upgrade_prices = []
upgrade_names = []
upgrade_dict = {}
suitable_upgrades = []

wait_for_element(driver=driver, element=cookie)
time.sleep(10)

while time.time() < five_min:
    wait_for_element(driver=driver, element=cookie)
    driver.find_element(*cookie).click()

    if time.time() > timeout:
        current_money = int(driver.find_element(*money).text.replace(',', ''))
        print(f"Current money: {current_money}")
        
        item_prices = driver.find_elements(*all_prices)
        upgrade_prices.clear()
        upgrade_names.clear()
        
        for price in item_prices:
            price_text = price.text
            if '-' in price_text:  # Ensure the price text has the format we expect
                try:
                    price_element = int(price_text.replace(',', '').split('-')[1].strip())
                    upgrade_name_element = price_text.split('-')[0].strip()
                    upgrade_prices.append(price_element)
                    upgrade_names.append(upgrade_name_element)
                except (ValueError, IndexError) as e:
                    print(f"Skipping an invalid item due to: {e}")
                    continue  # Skip items that don't match the expected format
                
        # Create the upgrade dictionary with valid upgrades
        upgrade_dict = {upgrade_names[n]: upgrade_prices[n] for n in range(len(upgrade_prices))}
        
        # Filter suitable upgrades
        suitable_upgrades.clear()
        item_list = list(upgrade_dict.items())
        for price in range(len(item_list)):
            if current_money >= item_list[price][1]:
                suitable_upgrades.append(item_list[price][0])

        # Select the most expensive affordable upgrade
        if suitable_upgrades:
            select_upgrade = suitable_upgrades[-1]
            print(f"Purchasing upgrade: {select_upgrade}")
            
            # Try clicking the appropriate upgrade button
            try:
                if " " in select_upgrade:
                    select_upgrade = select_upgrade.replace(" ","\\ ")
                driver.find_element(By.CSS_SELECTOR, value=f'#store #buy{select_upgrade}').click()
            except Exception as e:
                print(f"Failed to click the upgrade: {e}")

        timeout = time.time() + 5  # Reset the timeout for the next check

# Get final coins per second (CPS)
cps_gain = driver.find_element(*cps).text
print(f"Your coins per second at the end of the game was: {cps_gain}")

# quit_browser(driver)
