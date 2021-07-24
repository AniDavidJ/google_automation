from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver', options=options)

#browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')
browser.get('https://www.google.com/')
time.sleep(2)
search_input = browser.find_element_by_name('q')
search_input.send_keys('pathanamthitta')

time.sleep(2)
search_button = browser.find_element_by_css_selector('input[type="submit"]')
search_button.click()
time.sleep(2)