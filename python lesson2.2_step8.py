import time
from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element("css selector", "[name='firstname']")
    first_name.send_keys('gud')
    
    second_name = browser.find_element("css selector", "[name='lastname']")
    second_name.send_keys('gid')
    
    email = browser.find_element('css selector', '[name="email"]')
    email.send_keys('1@mail.com')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    name_file = 'file.txt'
    file_path = os.path.join(current_dir, name_file)
    
    send_file = browser.find_element('id', 'file')
    send_file.send_keys(file_path)
    
    button = browser.find_element('class name', 'btn')
    button.click()
finally:
    
    time.sleep(15)
    browser.quit()