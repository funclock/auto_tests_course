from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('[id="num1"]').text
    y = browser.find_element_by_css_selector('[id="num2"]').text

    key = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(key)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
