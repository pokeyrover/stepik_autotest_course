from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

wait = WebDriverWait(browser, 15)

try:
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    value = browser.find_element('id', 'input_value').text
    browser.execute_script('return arguments[0].scrollIntoView(true);', browser.find_element(By.ID, 'price'))
    x = calc(value)
    
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(x)
    
    button = browser.find_element(By.ID, 'solve')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()