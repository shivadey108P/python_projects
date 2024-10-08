from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CookiePage:
    
    def __init__(self, driver) -> None:
        self.driver = driver
        self.cookie = (By.ID, 'cookie')
        self.upgrades = (By.CSS_SELECTOR, '#store div')
        self.money = (By.ID, 'money')
        self.cps = (By.ID, 'cps')
        self.all_prices = (By.CSS_SELECTOR, '#store b')
        
    def get_url(self, url):
        self.driver.get(url)
        
    def get_money_data(self):
        return self.driver.find_element(*self.money).text
    
    def get_store_prices(self):
        return self.driver.find_elements(*self.upgrades)
        
    def click_cookie(self):
        self.driver.find_element(*self.cookie).click()
        
    def quit_browser(self):
        self.driver.quit()
    
    def wait_for_element(self, element):
        WebDriverWait(self.driver, 20).until(
    EC.visibility_of_element_located(element)
)