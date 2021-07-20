import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/simplevalidation.html')

# --- def ---#
def element_valid(element_id, text):
    email = driver.find_element_by_id(element_id)
    email.clear()
    email.send_keys(text)
    time.sleep(3)
    x_path = str('//*[@id="' + element_id + '"]')
    success = driver.find_element_by_xpath(x_path).get_attribute('data-jsv-field-isvalid')
    if success != 'true':
        message_target = driver.find_element_by_xpath(x_path).get_attribute('data-jsv-message-target')
        message = driver.find_element_by_id(message_target).text
        return message
    return 'true'

def select_menu(element_id, select_item):
    select = Select(driver.find_element_by_id(element_id))
    select.select_by_visible_text(select_item)
    time.sleep(3)
    x_path = str('//*[@id="' + element_id + '"]')
    success = driver.find_element_by_xpath(x_path).get_attribute('data-jsv-field-isvalid')
    if success != 'true':
        message_target = driver.find_element_by_xpath(x_path).get_attribute('data-jsv-message-target')
        message = driver.find_element_by_id(message_target).text
        return message
    return 'true'

def click_checkbox_or_radio(element_id):
    checkbox = driver.find_element_by_id(element_id)
    checkbox.click()
    x_path = str('//*[@id="' + element_id + '"]')
    success = driver.find_element_by_xpath(x_path).get_attribute('data-jsv-field-isvalid')
    time.sleep(3)
    if success != 'true':
        message_target = driver.find_element_by_xpath(x_path).get_attribute('data-jsv-message-target')
        message = driver.find_element_by_id(message_target).text
        return message
    return 'true'

# - - - - - - -
try:
    # e-mail
    assert element_valid('test-email', 'aeoiéghasdlufasd') == 'Please check your E-Mail format'
    assert element_valid('test-email', 'example@example.com') == 'Login does not exist'
    assert element_valid('test-email', 'yardy@yarr.com')

    # Desired Password
    assert element_valid('test-password', '123ab') == 'Should be between 6 and 20 characters'
    assert element_valid('test-password', '123ab123ab123ab123abc') == 'Should be between 6 and 20 characters'
    assert element_valid('test-password', '123abc')

    # Confirm Password
    assert element_valid('test-confirm-password', '123ab') == 'Does not match Desired Password'
    assert element_valid('test-confirm-password', '123abc')

    # Customer Number
    assert element_valid('test-customer-number', 'srgsergísefaefwea') == 'Should be a number'
    assert element_valid('test-customer-number', '12164132684613874')

    # Dealer Number
    assert element_valid('test-dealer-number', 'nalghs') == 'Should be a 4 character number'
    assert element_valid('test-dealer-number', 'nal125ghs') == 'Should be a 4 character number'
    assert element_valid('test-dealer-number', '465135') == 'Should be a 4 character number'
    assert element_valid('test-dealer-number', '1234')

    # Random Field
    assert element_valid('test-random-field', '465135') == 'Should contain "twelve"'
    assert element_valid('test-random-field', 'dkahfatwelveaghaeéfn')
    assert element_valid('test-random-field', 'twelve')

    # Date Field
    assert element_valid('test-date-field', '20200420') == 'Must match pattern YYYY-MM-DD'
    assert element_valid('test-date-field', '2020.04.20') == 'Must match pattern YYYY-MM-DD'
    #assert element_valid('test-date-field', datetime.date(0000, 0, 0)) == 'Must match pattern YYYY-MM-DD'
    assert element_valid('test-date-field', '2020-04-20')

    # URL Field
    assert element_valid('test-url-field', 'ausfbjdnidWEDOÉJJ') == 'Please enter a valid URL (starts with "http" or "https")'
    assert element_valid('test-url-field', 'https://www.python.org')

    # Random Textarea
    assert element_valid('test-random-textarea', 'i heart textarea') == 'Should be only letters and numbers'
    assert element_valid('test-random-textarea', 'ihearttextarea')

    # Card Type
    assert select_menu('test-card-type', 'MasterCard')
    assert select_menu('test-card-type', 'Select Card Type') == 'Please select a card type'
    assert select_menu('test-card-type', 'Visa')

    # Card Number
    assert element_valid('test-card-number', '4111111111111112') == 'Please check your credit card nubmer'
    assert element_valid('test-card-number', '4111111111111111')

    # Card CVV
    assert element_valid('test-card-cvv', 'asklfhew') == 'Should be a number between 3 and 4 characters'
    assert element_valid('test-card-cvv', '12') == 'Should be a number between 3 and 4 characters'
    assert element_valid('test-card-cvv', 'ab12')
    assert element_valid('test-card-cvv', '123')

    # Expiration Month
    assert select_menu('test-card-month', 'February')
    assert select_menu('test-card-month', 'Select Month') == 'Select a month'
    assert select_menu('test-card-month', 'December')

    # Expiration Year
    assert select_menu('test-card-year', '2018')
    assert select_menu('test-card-year', 'Select Year') == 'Select a year'
    assert select_menu('test-card-year', '2027')

    # Just a regular single checkbox
    click_checkbox_or_radio('test-single-checkbox')

    # Receive E-Mail Updates?
    click_checkbox_or_radio('test-save-email-no')
    click_checkbox_or_radio('test-save-email-yes')

    # Agree to terms of service?
    click_checkbox_or_radio('test-terms-service')

    # Agree to more stuff?
    click_checkbox_or_radio('test-terms-service-more')

    button = driver.find_element_by_id('test-button')
    button.click()
finally:
    driver.close()