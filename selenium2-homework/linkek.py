from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/')

## Lokátorral keresd ki az összes linket az oldalról.
table = driver.find_element_by_tag_name('tbody')
cells = table.find_elements_by_tag_name('td')

## Tárold a memóriában egy listában az összes linket.
links = []
for i in cells:
    links.append(i.text)

# A list tartalmát írd ki egy fájlba.
# Minden link egy új sorba kerüljön.
celfajl = open('list_of_links.txt', 'w')
for link in links:
    print(link, end='\n', file=celfajl)
celfajl.close()

# A kimenetre írd ki hány linket találtál

number_of_links = len(links)
print(number_of_links)

driver.close()
