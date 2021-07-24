from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver', options=options)
browser.get('https://www.youtube.com/')
time.sleep(2)
search_input1 = browser.find_element_by_name('search_query')
search_input1.send_keys('pathanamthitta')
time.sleep(2)
search_button1 = browser.find_element_by_css_selector('button[id="search-icon-legacy"]')
search_button1.click()
time.sleep(10)
