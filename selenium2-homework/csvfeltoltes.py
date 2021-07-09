import csv
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/another_form.html')

# A függvény egkeresi az id-t és kitörli a mezőt
def find_and_clear(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

# Küldés gomb
button_send = driver.find_element_by_id('submit')

# fájl beolvasása és táblázat kitöltése:
with open('table_in.csv', 'r', encoding='utf-8') as table:
    csv_reader = csv.reader(table, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        find_and_clear('fullname').send_keys(row[0])
        find_and_clear('email').send_keys(row[1])
        find_and_clear('dob').send_keys(row[2])
        find_and_clear('phone').send_keys(row[3])
        button_send.click()

# HTML táblázat .csv fájllá exportálása
driver.find_element_by_xpath('/html/body/main/div/button').click()

time.sleep(8)

driver.close()
# eredeti és a letöltött fájlok sorainak összehasonlítása:
with open('C:\\Users\\Brigi\\Downloads\\table.csv', 'r', encoding='utf-8') as new_table:
    new_csv_reader = csv.reader(new_table, delimiter=',')
    next(new_csv_reader)
    with open('table_in.csv', 'r', encoding='utf-8') as old_table:
        old_csv_reader = csv.reader(old_table, delimiter=',')
        next(old_csv_reader)
        new_list = list(new_csv_reader)
        old_list = list(old_csv_reader)
        for i in new_list and old_list:
            print('ok')

