from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9999/trickyelements.html')


el1 = driver.find_element_by_id('element1')
el2 = driver.find_element_by_id('element2')
el3 = driver.find_element_by_id('element3')
el4 = driver.find_element_by_id('element4')
el5 = driver.find_element_by_id ('element5')

button = driver.find_element_by_tag_name('button')
button.click()

result = driver.find_element_by_id('result')

if button.text + ' was clicked' == result.text:
    print('ok')
else:
    print('nem ok')
driver.close()