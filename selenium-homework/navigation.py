# A feladatod, hogy végiglátogassd az összes linket ezen az oldalon. Egy
# link meglátogatása akkor érvényes, ha a hozzá tartozó a html elemre rákattintottál,
# a megjelent új oldalnak ellenrőizted, hogy eggyezik az urlje az előzőleg használt
# a tag href-jével és sikeresen vissza navigáltál a főoldalra. (A tökéletes megoldás nem
# tartalmaz sor ismétléseket. Ezt mondjuk függvények írásával is elő tudod idézni.)

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://localhost:9999/general.html')

anchors = driver.find_elements_by_xpath('//header//small//a')

for a in anchors:
    a.click()
    if driver.current_url == a.get_attribute('href'):
        print(driver.current_url, 'sikeres')
    else:
        print(driver.current_url, 'sikertelen')
print('*' * 50)
while driver.current_url != 'http://localhost:9999/general.html':
    print(driver.current_url)
    driver.back()
driver.close()
