from selenium import webdriver

driver = webdriver.Chrome ( )
try:
    driver.get ('https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html')
    target_color = driver.find_element_by_id ('target_color').text
    print (target_color)
    table = driver.find_element_by_xpath ('/html/body/table')
    rows = table.find_elements_by_tag_name ('tr')
    color = ''
    main_window = driver.window_handles[0]
    for row in rows:
        cells = row.find_elements_by_tag_name ('td')
        for cell in cells:
            cell.click ( )
            new_window = driver.window_handles[1]
            driver.switch_to.window (new_window)
            color = driver.find_element_by_xpath ('/html/body/h1').text
            driver.close ( )
            driver.switch_to.window (main_window)
            if color == target_color:
                break
        if color == target_color:
            break
    number_of_guesses = driver.find_element_by_id ('numberOfGuesses').text
    print ("Number of guesses made: ", number_of_guesses)
finally:
    driver.close ( )
