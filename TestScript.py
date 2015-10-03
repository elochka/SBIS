__author__ = 'Asus'

import unittest
from LoginPage import LoginPage
from MainPage import MainPage
from StaffPage import StaffPage
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginPageTest(unittest.TestCase):
    def test(self):
        logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)
        driver = webdriver.Chrome()
        driver.get("http://fix-inside.tensor.ru")
        logging.info("Loading login page.")
        time.sleep(5)
        self.assertEqual("Вход в систему/СБИС", driver.title)
        logPage = LoginPage(driver)
        logPage.getLoginField().send_keys("check_rigth_user")
        logPage.getPasswordInput().send_keys("qwerty123")
        logPage.getloginButton().click()
        logging.info("Login process started")
        time.sleep(5) #wait for next page load
        self.assertEqual("СБИС", driver.title)
        logging.info("Login was successfull")
        time.sleep(5)

        mainPage = MainPage(driver)
        mainPage.getstaffLink().click()
        time.sleep(2)
        mainPage.getstaffLink().click()
        time.sleep(5)
        self.assertEqual("Сотрудники/СБИС", driver.title)
        logging.info("Staff page opened")

        staffPage = StaffPage(driver)
        staffPage.getorgLink().click()
        time.sleep(5)
        logging.info("Organizations list opened")






        driver.close()

if __name__ == '__main__':
    unittest.main()