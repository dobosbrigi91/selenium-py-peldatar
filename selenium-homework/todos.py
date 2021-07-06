from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9999/todo.html')

todos = driver.find_elements_by_class_name('done-false')
for dos in todos:
    print(dos.text)
