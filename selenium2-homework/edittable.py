import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/editable-table.html')
    
    ## a) Addj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
    # Két üres sor hozzáadása
    add_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/button')
    add_button.click()
    add_button.click()
    
    table = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody')
    rows = table.find_elements_by_tag_name('tr')

    # csv fájlból táblázat kitöltése
    with open('edittable.csv', 'r') as file:
        file_reader = csv.reader(file, delimiter=',')
        next(file_reader)
        for row in rows[-2:]:
            csv_sor = next(file_reader)
            csv_elem = 0
            cells = row.find_elements_by_tag_name('td')
            for cell in cells:
                cell_input = cell.find_element_by_tag_name('input')
                cell_value = cell_input.get_attribute('value')
                if cell_value == '' or cell_value == '0':
                    cell_input.clear()
                    elem = csv_sor[csv_elem]
                    cell_input.send_keys(elem)
                    csv_elem += 1
                    assert cell_input.get_attribute('value') == elem, 'valami nem jó'
    ##b) Ellenőrizd a kereső funkciót.

    search_input = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/input')
    search_input.send_keys('ball')
    print(len(rows))
    for row in rows:
        cells = row.find_elements_by_tag_name('td')
        for cell in cells:
            cell_input = cell.find_element_by_tag_name('input')
            cell_value = cell_input.get_attribute('value')
            if 'ball' in cell_value:
                print(rows.index(row), 'ok')
            else:
                print(False)

    ##c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.

    first = driver.find_element_by_xpath('//*[@id="1"]')
    first.clear()
    first.send_keys('kiscica')
    first_rename = driver.find_element_by_xpath('//*[@id="1"]')
    assert first == first_rename, 'nem'

finally:
    driver.close()