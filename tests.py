from selenium.webdriver.common.by import By

page = "login-header"
username_el = "username"
password_el = "password"
submit = "//button[@type='submit']"
expected_url = "localhost:4200/#/"
new_member = "new-member"

def open_url(driver, url):
   driver.get(url)
   driver.find_element(By.CLASS_NAME, page)


def add_field(driver, value, field):
   username_field = driver.find_element(By.NAME, field)
   username_field.clear()
   username_field.send_keys(value)


def add_credentials(driver, username, password):
   add_field(driver, username, username_el)
   add_field(driver, password, password_el)


def submit_form(driver):
   driver.find_element(By.XPATH, submit).click()


# def verify_url(driver, url):
#    assert expected_url == driver.current_url

def search_member_button(driver):
    driver.get(expected_url)
    # dropdown-content
    driver.find_element(By.CLASS_NAME, 'dropbtn').click()
    driver.find_element(By.CLASS_NAME,new_member).click()
    print(driver.find_element(By.CLASS_NAME,'text-center'))
    assert driver.find_element(By.CLASS_NAME,'text-center')=='Register New Member'