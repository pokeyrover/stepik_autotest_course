import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    
    value = browser.find_element('id', 'input_value').text
    x = calc(value)
    
    input = browser.find_element('id', 'answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', input)
    input.send_keys(x)
    
    check = browser.find_element('css selector', '[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    
    radio = browser.find_element('id', 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()
    
    button = browser.find_element('class name', 'btn')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()