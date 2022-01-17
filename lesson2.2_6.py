from selenium import webdriver
import time
from math import sin, log


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('[id="input_value"]').text
    key = log(abs(12 * sin(int(x))))

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(str(key))
    input2 = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    input2.click()
    input3 = browser.find_element_by_css_selector('[value="robots"]')
    input3.click()
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
