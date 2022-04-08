import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = browser.find_element('class name', 'btn')
    button.click()
    
    confim = browser.switch_to.alert
    confim.accept()
    
    x = browser.find_element('id', 'input_value').text
    y = calc(x)
    
    input = browser.find_element('id', 'answer')
    input.send_keys(y)
    
    browser.find_element('class name', 'btn').click()

finally:
    time.sleep(15)
    browser.quit()