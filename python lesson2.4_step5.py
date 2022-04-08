from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/cats.html')

browser.implicitly_wait(5)

browser.find_element_by_id('button').click()

browser.quit()