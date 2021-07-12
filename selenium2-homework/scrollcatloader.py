from selenium import webdriver
import time, requests
import os
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/scrolltoload.html')

    #load_more = driver.find_element_by_xpath('//div[@class="load-more-button"]/button')
    images_url = []
    n = 0
    for i in range(4):
        time.sleep(3)
        images = driver.find_elements_by_xpath('//div[@class="image"]')
        for j in images[-5:]:
            cica = str(j.find_element_by_tag_name('p').text).split(':')
            cicaname = str(n+1)+'_'+str(cica[1])
            src = j.find_element_by_tag_name('img').get_attribute('src')
            images_url.append(src)
            response = requests.get(images_url[n])
            n = n+1
            dir_cat = os.getcwd() + f"//cat/{cicaname}.png"
            with open(dir_cat, 'wb') as cats:
                cats.write(response.content)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
finally:
    driver.close()