from datetime import datetime, date, time, timezone
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import locale

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/forms.html')
locale.setlocale(locale.LC_ALL, 'hu_Hu')

nowutc = datetime.now(timezone.utc)

#Date:
driver.find_element_by_id('example-input-date').send_keys(nowutc.strftime("00%Y/%m/%d"))

#Date/Time:
driver.find_element_by_id('example-input-date-time').send_keys(nowutc.strftime('%Y/%m/%d/%X'))

#Date/Time local: - ##?
##driver.find_element_by_id('datetime-local').send_keys(nowutc.strftime('%Y/%m/%d'))
##driver.find_element_by_id('datetime-local').send_keys(nowutc.strftime('%x'))

#Month: - ## Az évet beírja a hónapot nem - ???
##driver.find_element_by_id('example-input-month').send_keys(nowutc.strftime('%Y. %B'))

#Week:
driver.find_element_by_id('example-input-week').send_keys(nowutc.strftime('%U'), nowutc.strftime('%Y'))

#Time:
driver.find_element_by_id('example-input-time').send_keys(nowutc.strftime('%H:%M'))
