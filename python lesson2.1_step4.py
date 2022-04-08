import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time

link = 'http://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element('id', "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element('id', "answer")
    input1.send_keys(y)

    checkbox = browser.find_element('id', "robotCheckbox")
    checkbox.click()

    radiobatton = browser.find_element('css selector', "[for='robotsRule']")
    radiobatton.click()

    button = browser.find_element('class name', "btn")
    button.click()

finally:
    
    time.sleep(15)
    browser.quit()
