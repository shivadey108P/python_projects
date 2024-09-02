from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options =  webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.python.org/')
upcoming_events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
upcoming_events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_dict = {}
for event in range(len(upcoming_events_time)):
    event_dict[event] = {
        'name': upcoming_events_name[event].text,
        'date': upcoming_events_time[event].text
    }
    
pprint(event_dict)
driver.quit()