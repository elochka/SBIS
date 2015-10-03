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
    def test(self):
        logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)
        driver = webdriver.Chrome()
        wait10sec = WebDriverWait(driver, 10)
        driver.get("http://fix-inside.tensor.ru")
        logging.info("Loading login page.")
        time.sleep(5)
        self.assertEqual("Вход в систему/СБИС", driver.title)

        logPage = LoginPage(driver)
        logPage.getLoginField().send_keys("check_rigth_user")
        logPage.getPasswordInput().send_keys("qwerty123")
        logPage.getloginButton().click()
        logging.info("Login process started")
        time.sleep(5)
        self.assertEqual("СБИС", driver.title)
        logging.info("Login was successfull")

        mainPage = MainPage(driver)
        wait10sec.until(lambda _: len(mainPage.getClosePopupLinks()) > 0)
        for link in mainPage.getClosePopupLinks():
            logging.info("Popup was closed")
            link.click()
            time.sleep(1)

        mainPage.getstaffLink().click()
        time.sleep(2)
        mainPage.getstaffLink().click()
        time.sleep(5)
        self.assertEqual("Сотрудники/СБИС", driver.title)
        logging.info("Staff page opened")

        staffPage = StaffPage(driver)
        #firstName = staffPage.getorgLink().text()
        staffPage.getorgLink().click()
        time.sleep(5)
        logging.info("Organizations list opened")
        # проверка: открылась форма с подразделениями







        driver.close()

if __name__ == '__main__':
    unittest.main()