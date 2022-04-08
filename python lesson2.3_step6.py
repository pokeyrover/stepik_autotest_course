import time
import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element('class name', 'trollface')
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = calc(browser.find_element('id', 'input_value').text)
    
    browser.find_element('id', 'answer').send_keys(x)
    
    browser.find_element('class name', 'btn').click()
    
finally:
    time.sleep(15)
    browser.quit()