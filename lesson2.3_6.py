from selenium import webdriver
import time
from math import log, sin


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector('[id="input_value"]').text
    key = log(abs(12 * sin(int(x))))
    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(str(key))
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
