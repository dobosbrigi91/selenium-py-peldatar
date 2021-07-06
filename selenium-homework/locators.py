from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9999/kitchensink.html')

openwindow = driver.find_element_by_id('openwindow')
openwindow_xpath = driver.find_element_by_xpath('//*[@id="openwindow"]')

print(openwindow_xpath.text)

cars = driver.find_element_by_name('cars')
cars_xpath = driver.find_element_by_xpath('//*[@name="cars"]')
print(cars_xpath.tag_name)
driver.close()