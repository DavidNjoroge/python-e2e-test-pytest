from selenium.webdriver.common.by import By

page = "login-header"
username_el = "username"
password_el = "password"
submit = "//button[@type='submit']"
expected_url = "http://payer-test-site.s3-website-ap-southeast-1.amazonaws.com/#/"
new_member = "//a[contains(@href, '#/new-member/')]"

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


def verify_url(driver, url):
   assert url == driver.current_url

def search_member_button(driver):
    # driver.find_element(By.CLASS_NAME, 'dropbtn').click()
    driver.find_element(By.XPATH,new_member).click()
    assert driver.find_element(By.CLASS_NAME)=='text-center'