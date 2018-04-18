#! /usr/bin/env python3.6

import unittest
from selenium import webdriver
import time
class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.get('localhost:4200')
        self.addCleanup(self.browser.quit)

    # def testPageTitle(self):
    #     self.assertTrue(self.browser.current_url, 'localhost:4200/#/loffgin')

    # def testLogin(self):
    #     self.browser.get
    def add_credentials(self,driver,username, password):
        username_el = "username"
        password_el = "password"
        self.add_field(driver,username, username_el)
        self.add_field(driver,password, password_el)

    def add_field(self,driver, value, field):
        username_field = driver.find_element_by_name(field)
        username_field.clear()
        username_field.send_keys(value)

    def testSubmit_form(self):
        driver = self.browser
        submit = "//button[@type='submit']"
        self.add_credentials(driver,'254726609646','0000')
        driver.find_element_by_xpath(submit).click()
        # time.sleep(5)
        # driver.implicitly_wait(190)
        # print('current_url',driver.current_url=='localhost:4200')
        self.assertEqual(driver.current_url,'http://localhost:4200/#/',"did not login successfully or sever took long")
if __name__ == '__main__':
    unittest.main()