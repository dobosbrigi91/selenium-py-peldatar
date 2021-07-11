from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html')

    ###Az oldalon találhotó összes beágyazott videót indítsa el és állítsa meg.

    ##HTML5 video built in controls
    first_video = driver.find_element_by_id('html5video')
    first_video.click()
    first_video.send_keys(Keys.SPACE)
    time.sleep(5)
    first_video.send_keys(Keys.SPACE)

    #HTML5 video with custom controls
    second_video = driver.find_element_by_id('video1')
    play_and_pause_button = driver.find_element_by_xpath('/html/body/div/button[1]')
    play_and_pause_button.click()
    time.sleep(5)
    play_and_pause_button.click()

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)

    ##Embedded youtube video in iframe
    third_video = driver.find_element_by_xpath("//iframe[contains(@src,'https://www.youtube.com')]")
    driver.switch_to.frame(third_video)
    play_button = driver.find_element_by_xpath("//button[@aria-label='Lejátszás']")
    play_button.click()
    time.sleep(2)
    pause_button = driver.find_element_by_xpath("//button[@aria-label='Szüneteltetés (k)']")
    pause_button.click()
finally:
    driver.close()