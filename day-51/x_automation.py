from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
import time

load_dotenv()

EMAIL = os.environ['X_EMAIL']
PASSWORD = os.environ['X_PASSWORD']
USERNAME = os.environ['X_USERNAME']
PROMISED_DOWN = float(os.environ['PROMISED_DOWNLOAD_SPEED'])
PROMISED_UP = float(os.environ['PROMISED_UPLOAD_SPEED'])

class InternetSpeedXBot:
    def __init__(self) :
        self.chrome_options = webdriver.ChromeOptions()
        self.preferences = {
            "profile.default_content_setting_values.geolocation": 1,  # 1 to allow, 2 to block
            "profile.default_content_setting_values.notifications": 2,  # 1 to allow, 2 to block
            "profile.default_content_setting_values.media_stream": 2,  # For camera and microphone access
        }

        self.chrome_options.add_experimental_option("prefs", self.preferences)
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options= self.chrome_options)
        self.up = 0
        self.down = 0
        self.reject_all_policy_btn = (By.ID, "onetrust-reject-all-handler")
        self.close_notification = (By.CSS_SELECTOR, ".notification a")
        self.test_go_btn = (By.CLASS_NAME, "start-text")
        self.download_speed_results = (By.XPATH, "//span[@class='result-data-large number result-data-value download-speed']")
        self.upload_speed_results = (By.XPATH, "//span[@class='result-data-large number result-data-value upload-speed']")
        
        self.sign_in = (By.XPATH, "//span[text()='Sign in']")
        self.email_input = (By.NAME, "text")
        self.next_btn_in_email = (By.XPATH, "//span[text()='Next']")
        self.password_input = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//span[text()='Log in']")
        self.post_input = (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        self.post_btn = (By.XPATH, "//span[text()='Post']")
        self.post_three_dot_icon = (By.XPATH, "//span[text()='First time using this post, how board to set up an account and post here ']//preceding::div[7]")
        self.delete_post = (By.XPATH, "//span[text()='Delete']")
        
    def wait_for_element(self, element, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(element)
        )

    def quit_browser(self):
        self.driver.quit()
        
    def close_current_window(self):
        self.driver.close()
        
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_internet_speed(self):
        # self.driver.maximize_window()
        self.driver.get('https://www.speedtest.net/')
        self.wait_for_element(element=self.test_go_btn, timeout=120)
        time.sleep(3)
        self.driver.find_element(*self.reject_all_policy_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.close_notification).click()
        time.sleep(2)
        self.go_button = self.driver.find_element(*self.test_go_btn)
        # self.scroll_to_element(self.go_button)
        # time.sleep(1)
        self.go_button.click()
        time.sleep(60)
        self.wait_for_element(element=self.download_speed_results, timeout=20)
        self.down = float(self.driver.find_element(*self.download_speed_results).text)
        self.up = float(self.driver.find_element(*self.upload_speed_results).text)
        print(f"download speed = {self.down}")
        print(f"Upload Speed = {self.up}")
        self.close_current_window()
        
    
    def post_at_x_to_network_provider(self):
        if PROMISED_DOWN > self.down and PROMISED_UP > self.up:
            self.message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 100down/100up?"
            try:
                self.driver = webdriver.Chrome(options=self.chrome_options)
                self.driver.maximize_window()
                self.driver.get("https://x.com/")
                self.wait_for_element(element=self.sign_in)
                self.driver.find_element(*self.sign_in).click()
                self.wait_for_element(element=self.email_input)
                time.sleep(1)
                self.driver.find_element(*self.email_input).send_keys(EMAIL, Keys.ENTER)
                self.wait_for_element(self.password_input)
                time.sleep(1)
                self.driver.find_element(*self.password_input).send_keys(PASSWORD, Keys.ENTER)
                self.wait_for_element(self.post_input)
                time.sleep(1)
                self.driver.find_element(*self.post_input).send_keys(self.message)
                time.sleep(1)
                self.driver.find_element(*self.post_btn).click()
                post_xpath = f"//span[text()='{self.message}']"
                post = (By.XPATH, post_xpath)
                self.wait_for_element(element=post, timeout=15)
                post_visible = self.driver.find_element(*post)
                assert post_visible.is_displayed(), "Post is not visible"
                print(post_visible.text)
            # delete_post_xpath
            except selenium.common.exceptions.InvalidSessionIdException as e:
                print(f"Session expired: {e}")
            finally:
                self.quit_browser()  # Ensure browser is properly closed
            
            
    
bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.post_at_x_to_network_provider()