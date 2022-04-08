import math
import time
from tkinter.tix import Select

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    cargo = browser.find_element("id", "treasure")
    value = cargo.get_attribute("valuex")
    y = calc(value)
    
    input = browser.find_element("id", "answer")
    input.send_keys(y)
    
    checkbox = browser.find_element("id", "robotCheckbox")
    checkbox.click()
    
    radio = browser.find_element("id", "robotsRule")
    radio.click()
    
    button = browser.find_element("class name", "btn")
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()
