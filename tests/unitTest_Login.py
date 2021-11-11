import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


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
        driver.get("http://127.0.0.1:8004")
        # assert "Logged in"
        try:
            driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[5]/a").click()
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
