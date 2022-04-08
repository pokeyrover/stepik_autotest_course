import time

from selenium import webdriver


link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

from selenium.webdriver.support.ui import Select

try:
    num1 = int(browser.find_element('id', 'num1').text)
    num2 = int(browser.find_element('id', 'num2').text)
    
    answer = str(num1 + num2)
    
    lst = Select(browser.find_element('id', 'dropdown'))
    lst.select_by_visible_text(answer)
    
    browser.find_element('class name', 'btn').click()
    
finally:
    time.sleep(15)
    browser.quit()

