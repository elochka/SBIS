__author__ = 'Asus'

import unittest
import logging
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from LoginPage import LoginPage
from MainPage import MainPage
from StaffPage import StaffPage


class LoginPageTest(unittest.TestCase):
    def setUp(self):
        # https://docs.python.org/2/howto/logging-cookbook.html#multiple-handlers-and-formatters
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler('test.log')
        fileHandler.setLevel(logging.DEBUG)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        self.log.addHandler(consoleHandler)
        self.log.addHandler(fileHandler)

        self.driver = webdriver.Chrome()
        self.wait10sec = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def waitAndClosePopup(self):
        mainPage = MainPage(self.driver)
        try:
            self.wait10sec.until(lambda _: len(mainPage.getClosePopupLinks()) > 0)
            for link in mainPage.getClosePopupLinks():
                logging.info("Popup was closed")
                link.click()
                time.sleep(1)
        except:
            logging.info("Popup was not found")

    # https://stackoverflow.com/questions/27948420/click-at-at-an-arbitrary-position-in-web-browser-with-selenium-2-python-binding
    def forceClick(self, element, xoffset=5, yoffset=5):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, xoffset, yoffset)
        action.click()
        action.perform()

    def test_main(self):
        self.driver.get("http://fix-inside.tensor.ru")
        self.log.info("Loading login page.")
        time.sleep(5)
        self.assertEqual("Вход в систему/СБИС", self.driver.title)

        logPage = LoginPage(self.driver)
        logPage.getLoginField().send_keys("check_rigth_user")
        logPage.getPasswordInput().send_keys("qwerty123")
        logPage.getloginButton().click()
        self.log.info("Login process was started")
        time.sleep(5)
        self.assertEqual("СБИС", self.driver.title)
        self.log.info("Login was successful")

        self.waitAndClosePopup()

        mainPage = MainPage(self.driver)
        self.forceClick(mainPage.getstaffLink())
        time.sleep(5)
        self.forceClick(mainPage.getstaffLink())
        time.sleep(20) # на моём ноутбуке страница грузится очень долго
        self.assertEqual("Сотрудники/СБИС", self.driver.title)
        self.log.info("Staff page was opened")

        staffPage = StaffPage(self.driver)
        link = staffPage.getorgLink()
        firstName = link.text
        staffPage.getorgLink().click()
        time.sleep(5)
        self.assertEqual(staffPage.isOrgFormVisible(), True)
        self.log.info("Organizations list was opened")

        staffPage.getchangeOrg().click()
        time.sleep(5)
        secondName = staffPage.getorgLink().text
        self.assertNotEqual(firstName, secondName)
        self.log.info("Link name was changed")

        staffPage.getsearchField().send_keys("Белова Олеся Александровна")
        time.sleep(5)
        self.assertIn("Белова Олеся", staffPage.getemployeeResult().text)
        self.log.info("Employee was found")

        staffPage.getemployeeResult().click()
        time.sleep(10)
        self.assertEqual(staffPage.isEmployeeCardVisible(), True)
        self.log.info("Employee card was opened")

        staffPage.getcloseCardButton().click()
        time.sleep(5)
        self.assertEqual(staffPage.isEmployeeCardVisible(), False)
        self.log.info("Employee card was closed")

        staffPage.getuserNameLink().click()
        time.sleep(5)
        self.assertEqual(staffPage.isUserMenuVisible(), True)
        self.log.info("User menu was opened")

        staffPage.getlogOutLink().click()
        time.sleep(5)
        self.assertEqual("Вход в систему/СБИС", self.driver.title)
        self.log.info("Logout was successful")

        time.sleep(10)

if __name__ == '__main__':
    unittest.main()