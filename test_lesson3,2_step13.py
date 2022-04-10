import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


    
def test_link1():
        
    try:
        
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
            
        input1 = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        input1.send_keys("Igr")
    
        input2 = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        input2.send_keys("Rex")
    
        input3 = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        input3.send_keys("email.l@mail.com")
    
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        time.sleep(1)
    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    
        welcome_text = welcome_text_elt.text
    
        assert "Congratulations! You have successfully registered!" == welcome_text, \
            "Welcome text not found"
            
    finally:
        
        time.sleep(15)
        browser.quit()
    
def test_link2():
        
    try:
        
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
            
        input1 = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        input1.send_keys("Igr")
    
        input2 = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        input2.send_keys("Rex")
    
        input3 = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        input3.send_keys("email.l@mail.com")
    
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        time.sleep(1)
    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    
        welcome_text = welcome_text_elt.text
    
        assert "Congratulations! You have successfully registered!" == welcome_text, \
            "Welcome text not found"
    
    finally:
    
        time.sleep(15)
        browser.quit()            
            
