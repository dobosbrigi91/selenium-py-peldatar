import csv

from selenium import webdriver
import pprint

driver = webdriver.Chrome()
a_char = []

try:
    driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/pagination.html')
    while True:
        table = driver.find_element_by_xpath('//*[@id="contacts-table"]/tbody')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name('td')
            data_row['id'] = cells[0].text
            data_row['first_name'] = cells[1].text
            data_row['second_name'] = cells[2].text
            data_row['surname'] = cells[3].text
            data_row['second_surname'] = cells[4].text
            data_row['birth_date'] = cells[5].text
            first_char = cells[1].text[0]
            if first_char == 'A':
                a_char.append(data_row)
        next_button = driver.find_element_by_id('next')
        if not next_button.is_enabled():
            with open('abetusek.csv', 'w') as file:
                fieldnames = ['id', 'first_name', 'second_name', 'surname', 'second_surname', 'birth_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rowdicts=a_char)
        else:
            next_button.click()
finally:
    driver.close()

