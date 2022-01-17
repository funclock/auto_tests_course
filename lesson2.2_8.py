from selenium import webdriver
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys('Сергей')
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('Кисленко')
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys('123@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector('[id="file"]')
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
