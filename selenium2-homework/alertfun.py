from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/alert_playground.html')

    ##A tanultak alapján az összes alert funkcióra írj selenium kódot.

    ##alert
    alert_button = driver.find_element_by_xpath('/html/body/div/div[2]/input[@name="alert"]')
    alert_button.click()
    alert = driver.switch_to.alert
    alert.accept()

    ##confirmation box
    confirmation_box_button = driver.find_element_by_xpath('/html/body/div/div[2]/input[@name="confirmation"]')
    confirmation_box_button.click()
    confirmation_box = driver.switch_to.alert
    confirmation_box.accept()

    ##prompt
    ## A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.
    prompt_button = driver.find_element_by_xpath('/html/body/div/div[2]/input[@name="prompt"]')
    prompt_button.click()
    prompt = driver.switch_to.alert
    prompt.send_keys('Szia')
    prompt.accept()
    you_entered = driver.find_element_by_id('demo').text
    assert (you_entered == 'You entered: Szia')

    ##double click
    actionChains = ActionChains(driver)
    double_click_button = driver.find_element_by_id('double-click')
    actionChains.double_click(double_click_button).perform()
    double_click = driver.switch_to.alert
    double_click.accept()
finally:
    driver.close()