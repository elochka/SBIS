__author__ = 'Asus'

import unittest
from LoginPage import LoginPage
from MainPage import MainPage
from StaffPage import StaffPage
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class LoginPageTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)
        self.log = logging.getLogger(__name__)
        self.driver = webdriver.Chrome()
        #self.driver.set_window_size(1280, 1024)
        self.wait10sec = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()

    def waitAndClosePopup(self):
        mainPage = MainPage(self.driver)
        self.wait10sec.until(lambda _: len(mainPage.getClosePopupLinks()) > 0)
        for link in mainPage.getClosePopupLinks():
            logging.info("Popup was closed")
            link.click()
            time.sleep(1)


    def test_main(self):
        self.driver.get("http://fix-inside.tensor.ru")
        self.log.info("Loading login page.")
        time.sleep(5)
        self.assertEqual("Вход в систему/СБИС", self.driver.title)

        logPage = LoginPage(self.driver)
        logPage.getLoginField().send_keys("check_rigth_user")
        logPage.getPasswordInput().send_keys("qwerty123")
        logPage.getloginButton().click()
        self.log.info("Login process started")
        time.sleep(5)
        self.assertEqual("СБИС", self.driver.title)
        self.log.info("Login was successfull")

        self.waitAndClosePopup()

        mainPage = MainPage(self.driver)
        mainPage.getstaffLink().click()
        time.sleep(2)
        mainPage.getstaffLink().click()
        time.sleep(5)
        self.assertEqual("Сотрудники/СБИС", self.driver.title)
        self.log.info("Staff page opened")

        staffPage = StaffPage(self.driver)
        #firstName = staffPage.getorgLink().text()
        staffPage.getorgLink().click()
        time.sleep(5)
        self.log.info("Organizations list opened")
        # проверка: открылась форма с подразделениями


if __name__ == '__main__':
    unittest.main()