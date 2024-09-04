from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

timeout = time.time() + 5
five_min = time.time() + 60*1



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

cookie = (By.ID, 'cookie')
upgrades = (By.CSS_SELECTOR, '#store div')
money = (By.ID, 'money')
cps = (By.ID, 'cps')
all_prices = (By.CSS_SELECTOR, '#store b')

def wait_for_element(driver, element):
    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(element))
        
def quit_browser(driver):
    driver.quit()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

upgrade_prices=[]
upgrade_names=[]
upgrade_dict = {}
suitable_upgrades = []

while time.time() < five_min:
    wait_for_element(driver=driver,element=cookie)
    driver.find_element(*cookie).click()
    
    if time.time() > timeout:
        current_money = int(driver.find_element(*money).text)
        print(current_money)
        item_prices = driver.find_elements(*all_prices)
        for price in item_prices:
            price_element = int(price.text.replace(',','').split('-')[1].strip())
            upgrade_prices.append(price_element)
            upgrade_name_element = price.text.split('-')[0].strip()
            upgrade_names.append(upgrade_name_element)
        
        for n in range(len(upgrade_prices)):
            upgrade_dict[upgrade_names[n]] = upgrade_prices[n]
            
        item_list = list(upgrade_dict.items())
            
        for price in range(len(upgrade_dict)):
            if item_list[price][1] < current_money < item_list[price+1][1]:
                suitable_upgrades.append(item_list[price][0])
        
        if len(suitable_upgrades) > 1:
            select_upgrade = suitable_upgrades[-1]
        else:
            select_upgrade = suitable_upgrades[0]
        
        driver.find_element(By.CSS_SELECTOR, value=f'#store buy{select_upgrade}')
        
        timeout = time.time() + 5
        
cps_gain = driver.find_element(*cps).text

print(f"Your coins per second at the end of the game was:{cps_gain}")
    
quit_browser(driver=driver)



