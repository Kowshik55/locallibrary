import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "admin"
        pwd = "admin123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8004/admin")
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[1]/input").send_keys(user)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[2]/input[1]").send_keys(pwd)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[3]/input").click()
        time.sleep(3)
        #CLick on genres
        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[4]/th/a").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[2]/table/tbody/tr[1]/td/input").click()
        time.sleep(3)
        # select label and delete action
        driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[1]/label/select").send_keys("delete_selected")
        time.sleep(3)
        # Click on go button
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div/form/div[1]/button").click()
        time.sleep(5)
        # Click on Yes am sure button
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/div/input[4]").click()
        time.sleep(5)
        try:
            # attempt to find the 'Logout' button - if found, logged in
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[3]")
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
