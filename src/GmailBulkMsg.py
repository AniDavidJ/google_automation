from selenium import webdriver
import time
import pandas as pd
from config import EMAIL, PASSWORD

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver', options=options)
#browser.maximize_window()
browser.get('http://www.gmail.com/')
time.sleep(2)
email_field = browser.find_element_by_css_selector('input[type="email"]')
email_field.send_keys(EMAIL)
time.sleep(2)
next_button = browser.find_element_by_class_name('VfPpkd-LgbsSe')
next_button.click()
time.sleep(2)
password_field = browser.find_element_by_css_selector('input[class="whsOnd zHQkBf"]')
password_field.send_keys(PASSWORD)
login_button = browser.find_element_by_class_name('VfPpkd-LgbsSe')
login_button.click()
time.sleep(10)


dataframe = pd.read_excel(r'C:\Users\TOSHIBA\Desktop\PythonProject\python-google-automation\src\data.xlsx')
for i in dataframe.index:
   # print(dataframe.loc[i])
    time.sleep(2)
    compose_btn = browser.find_element_by_css_selector('.T-I.T-I-KE.L3')
    compose_btn.click()
    time.sleep(2)
    to_field = browser.find_element_by_name('to')
    to_field.send_keys(dataframe.loc[i]['Email'])
    subject_field = browser.find_element_by_name('subjectbox')
    subject_field.send_keys('Application')
    body_field = browser.find_element_by_css_selector('.Am.Al.editable.LW-avf.tS-tW')
    body_content = f""" 
    Dear {dataframe.loc[i]['Name']},
    Data Analyst is important topic for analysis the data.

    """
    body_field.send_keys(body_content)
    send_mail = browser.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
    send_mail.click()
    time.sleep(5)


