from selenium import webdriver
from os import getcwd
import time

try:
    driver = webdriver.Chrome()
    driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/dragndrop2.html')

    time.sleep(3)

    cwd = getcwd()

    js_drag_drop = open(cwd + '\\dnd.js', 'r').read()

    items = driver.find_elements_by_xpath('//*[@id="Todo"]/li')
    target = driver.find_element_by_xpath('//*[@id="Doing"]')

    for item in items:
        driver.execute_script(js_drag_drop, item, target)
finally:
    driver.close()