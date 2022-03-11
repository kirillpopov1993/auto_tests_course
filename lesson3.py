from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element_by_id("num1")
    x_element1 = element1.text
    element2 = browser.find_element_by_id("num2")
    x_element2 = element2.text
    sumNum = str(int(x_element1) + int(x_element2))
    print(sumNum)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sumNum) 
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # ищем элемент с текстом "Python"
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    